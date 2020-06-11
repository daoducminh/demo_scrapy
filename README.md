# IT4853 - Nhom 1

## Prerequisite

- `python3-venv`
- ElasticSearch instance
- Docker

## Installation

1. Create python virtual environment: `virtualenv .virtualenvs`
2. Install python modules: `.virtualenvs/bin/python -m pip install .`

## Usage

1. Start Splash using Docker: `docker run -d -p 8050:8050 scrapinghub/splash`
2. Start crawling: `.virtualenvs/bin/python -m scrapy crawl news`
    - To enable logging, open file `demo/spider/news` and remove `'LOG_ENABLED': False,` in `custom_settings` 