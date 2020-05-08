# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import remove_tags


def remove_quote_symbol(text):
    return text[1:-1]


class Article(Item):
    title = Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join()
    )
    url = Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join()
    )


class Quote(Item):
    content = Field(
        input_processor=MapCompose(remove_tags, remove_quote_symbol),
        output_processor=Join()
    )
    author = Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join()
    )
    tags = Field(
        input_processor=MapCompose(remove_tags),
        # output_processor=Join()
    )


class Author(Item):
    name = Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join()
    )
    born_date = Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join()
    )
    born_location = Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join()
    )
    description = Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join()
    )
