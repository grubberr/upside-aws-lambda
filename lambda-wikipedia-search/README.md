# Lambda Wikipedia Search function
Lambda function which searches Wikipedia article and returns 2 numbers for every article:
  1. `latest_update_time` - last time in UTC when the article was updated.
  2. `number_updates_last_month` - how many times the article was updated in the current month.

## Usage

### Deployment

In order to deploy the example, you need to do next steps:

#### Setting Up Serverless Framework with `serverless-python-requirements` plugin

```bash
npm install -g serverless
serverless plugin install -n serverless-python-requirements
```

#### Settings Up AWS Credentials
https://www.serverless.com/framework/docs/providers/aws/guide/credentials

#### Deploy lambda function to AWS Lambda service

```
serverless deploy
```

### Invocation

After successful deployment, you can invoke the deployed function by using the following command:

```bash
serverless invoke --function lambda_handler --data '{"title": "Python_(programming_language)"}'
```

Which should result in response similar to the following:

```json
{
    "title": "Python_(programming_language)",
    "normalized_title": "Python (programming language)",
    "latest_update_time": "2022-09-04T17:54:12Z",
    "number_updates_last_month": 7,
    "found": true
}
```

### Local development

You can invoke your function locally by using the following command:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt
serverless invoke local --function lambda_handler --data '{"title": "Python_(programming_language)"}'
```

Which should result in response similar to the following:

```
{
    "title": "Python_(programming_language)",
    "normalized_title": "Python (programming language)",
    "latest_update_time": "2022-09-04T17:54:12Z",
    "number_updates_last_month": 7,
    "found": true
}
```
