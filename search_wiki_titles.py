#!/usr/bin/env python3

import json
import logging

import boto3


FUNCTION_NAME = "lambda-wikipedia-search-dev-lambda_handler"

titles = [
    "Washington,_D.C.",
    "United States",
    "Ukraine",
    "DALL-E",
    "Stable Diffusion",
    "Python_(programming_language)",
    "Go (programming language)",
    "Microservices",
    "Amazon_Web_Services",
    "AWS Lambda",
    "Java (programming language)"
]

client = boto3.client("lambda")


def search_wiki(title):
    payload = json.dumps({"title": title}).encode("utf-8")

    response = client.invoke(
        FunctionName=FUNCTION_NAME,
        InvocationType="RequestResponse",
        Payload=payload)

    response_payload = response["Payload"].read()
    if response.get("FunctionError") == "Unhandled":
        logging.error(response_payload)
        return {}
    return json.loads(response_payload)


def main():
    for title in titles:
        response = search_wiki(title)
        if response.get("found"):
            response.pop("found")
            print(json.dumps(response))


if __name__ == "__main__":
    main()
