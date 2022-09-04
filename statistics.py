#!/usr/bin/env python3

import json
import argparse

import pandas


def main(filename):
    data = []
    with open(filename) as fp:
        for line in fp:
            data.append(json.loads(line))

    df = pandas.json_normalize(data)
    df = df[df["number_updates_last_month"] <= 2]
    print("The sum of the updates:", df["number_updates_last_month"].sum())
    print("The mean value of the updates:", df["number_updates_last_month"].mean())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="jsonl file, result from search_wiki_titles.py script")
    args = parser.parse_args()
    main(args.filename)
