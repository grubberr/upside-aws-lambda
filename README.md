# Search Wiki
The scripts which demonstrate using lambda function [lambda-wikipedia-search](https://github.com/grubberr/upside-aws-lambda/tree/main/lambda-wikipedia-search).
The `search_wiki_titles.py` script searches multiple article titles on Wikipedia and returns 2 numbers for every article:
  1. `latest_update_time` - last time in UTC when the article was updated.
  2. `number_updates_last_month` - how many times the article was updated in the current month.

The `statistics.py` takes the result from the previous script and calculates
the sum of the updates for all articles, and the mean value of the updates for all articles.

## Usage
### Deployment
Deploy lambda function [lambda-wikipedia-search](https://github.com/grubberr/upside-aws-lambda/blob/main/lambda-wikipedia-search/README.md)

```bash
python3 -m venv .venv
. .venv/bin/activate
```

### Invocation

After successful deployment, you can invoke the scripts:

```bash
python3 search_wiki_titles.py > wiki_result.jsonl
python3 statistics.py wiki_result.jsonl
```
