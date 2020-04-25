# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json
import pysolr


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jsonl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class PySolr(object):
    def open_spider(self, spider):
        self.solr = pysolr.Solr(
            'http://localhost:8983/solr/test', always_commit=True)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.solr.add(item)
        return item
