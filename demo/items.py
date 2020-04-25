# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import remove_tags


class Article(Item):
    title = Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join()
    )
    url = Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join()
    )
