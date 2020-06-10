# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.http.response import Response
from scrapy.loader import ItemLoader
from scrapy_splash import SplashRequest, SplashResponse

JS_SCRIPT = "document.getElementById('zone_menu_trai_header').dispatchEvent(new MouseEvent('mouseover', { 'bubbles': true }));"
VPAGE = '?vpage={}'


class NewsSpider(Spider):
    name = 'news'
    start_news_urls = 'https://www.24h.com.vn/'

    custom_settings = {
        'ITEM_PIPELINES': {
            'demo.pipelines.RemoveDuplicatedPipeline': 1,
            'demo.pipelines.JsonWriterPipeline': 100,
            # 'demo.pipelines.MongoDBPipeline': 1,
            # 'demo.pipelines.ElasticSearchPipeline': 1
        },
        # 'LOG_ENABLED': False,
        'DEFAULT_REQUEST_HEADERS': {
        }
    }

    def start_requests(self):
        yield SplashRequest(
            url=self.start_news_urls,
            callback=self.parse_homepage,
            args={
                'js_source': JS_SCRIPT
            }
        )

    def parse_homepage(self, response: SplashResponse):
        # columns = response.css('#zone_menu_trai_header ul li a')
        column_list = response.xpath(
            "//div[@id='zone_menu_trai_header']//li/a")
        for c in column_list[1:4]:
            url = c.xpath('@href').get()
            column = c.xpath('text()').get()
            url = response.urljoin(url)
            for i in range(1, 3):
                yield Request(
                    url=url + VPAGE.format(i),
                    callback=self.parse_page,
                    cb_kwargs=dict(column=column)
                )

    def parse_page(self, response, column):
        items = response.xpath('//article/header//a')
        for item in items:
            article = {
                'title': item.xpath('text()').get(),
                'column': column,
                'url': item.xpath('@href').get()
            }
            yield article
