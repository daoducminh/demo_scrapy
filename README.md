# Demo Scrapy and Flask

## Installation

- Scrapy and Flask: `pip3 install scrapy flask`
- Solr: Download [Solr 8.5.1](https://www.apache.org/dyn/closer.lua/lucene/solr/8.5.1/solr-8.5.1.tgz) and extract. In `solr-8.5.1` folder, run: `bin/solr start`

## Usage

1. Scrapy:
- In `solr-8.5.1` folder, run: `bin/solr create -c test`
- In `demo_scrapy` folder, run: `scrapy crawl test`

2. Flask:
- In `demo_scrapy` folder, run:

```bash
export FLASK_APP=test_flask.py
flask run
```