# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.http.response import Response
from scrapy.loader import ItemLoader


class TestSpider(Spider):
    name = 'test'
    start_urls = ['https://www.24h.com.vn/cong-nghe-thong-tin-c55.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            # 'demo.pipelines.JsonWriterPipeline': 1,
            'demo.pipelines.PySolr': 1
        },
        'DEFAULT_REQUEST_HEADERS': {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'
        }
    }

    def parse(self, response):
        items = response.xpath('//article/header//a')
        for item in items:
            article = {
                'title': item.xpath('text()').get(),
                'url': item.xpath('@href').get()
            }
            yield article
