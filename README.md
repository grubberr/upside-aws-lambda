# Search Wiki
The scripts which demonstrate using lambda function [lambda-wikipedia-search](https://github.com/grubberr/upside-aws-lambda/tree/main/lambda-wikipedia-search).
The `search_wiki_titles.py` searches multiple article titles on Wikipedia and returns JSON statistic results for every title.
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
