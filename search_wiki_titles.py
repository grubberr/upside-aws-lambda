#!/usr/bin/env python3

import json
import boto3


REGION = "us-east-1"
FUNCTION_NAME = "upside-aws-lambda-dev-hello"

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

client = boto3.client("lambda", region_name=REGION)

def search_wiki(title):
    payload = json.dumps({"title": title}).encode("utf-8")

    response = client.invoke(
        FunctionName=FUNCTION_NAME,
        InvocationType="RequestResponse",
        Payload=payload)

    return json.loads(response["Payload"].read())

def main():
    for title in titles:
        response = search_wiki(title)
        if response["found"]:
            response.pop("found")
            print(json.dumps(response))

if __name__ == "__main__":
    main()
