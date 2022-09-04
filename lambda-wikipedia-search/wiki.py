#!/usr/bin/env python3
#
# https://www.mediawiki.org/wiki/API:Query#API_documentation
# https://www.mediawiki.org/wiki/API:Revisions
#


import datetime

import requests
from dateutil import parser


class WikiException(Exception):
    pass


class Wiki:
    base_url = "https://en.wikipedia.org/w/api.php"
    base_params = {
        "action": "query",
        "prop": "revisions",
        "titles": None,
        "rvprop": "timestamp",
        "format": "json",
        "rvlimit": 20,
    }

    def __run_loop(self, title):
        start_of_month = datetime.datetime.now(tz=datetime.timezone.utc).replace(
            microsecond=0, second=0, minute=0, hour=0, day=1
        )
        params = {**self.base_params, "titles": title}

        while True:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            response_json = response.json()
            if "error" in response_json:
                raise WikiException(response_json)

            query = response_json.get("query")
            if not query:
                return

            if self.normalized_title is None:
                self.normalized_title = title
                for item in query.get("normalized", []):
                    if item["from"] == self.normalized_title:
                        self.normalized_title = item["to"]

            for page in query["pages"].values():
                if page["title"] == self.normalized_title:
                    for revision in page.get("revisions", []):
                        if self.latest_update_time is None:
                            self.latest_update_time = revision["timestamp"]
                        if self.number_updates_last_month is None:
                            self.number_updates_last_month = 0
                        timestamp = parser.isoparse(revision["timestamp"])
                        if timestamp < start_of_month:
                            return
                        self.number_updates_last_month += 1

            rvcontinue = response_json.get("continue", {}).get("rvcontinue")
            if not rvcontinue:
                break
            params["rvcontinue"] = rvcontinue

    def query(self, title):
        self.normalized_title = None
        self.latest_update_time = None
        self.number_updates_last_month = None

        self.__run_loop(title)

        return {
            "title": title,
            "normalized_title": self.normalized_title,
            "latest_update_time": self.latest_update_time,
            "number_updates_last_month": self.number_updates_last_month,
            "found": bool(self.latest_update_time),
        }
