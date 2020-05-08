# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json
import pymongo
from elasticsearch import Elasticsearch
import pysolr


class JsonQuotesWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('quotes.json', 'w')
        self.file.write('[\n')

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item))+',\n'
        self.file.write(line)
        return item


class JsonAuthorsWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('authors.json', 'w')
        self.file.write('[\n')

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item))+',\n'
        self.file.write(line)
        return item


class ElasticSearchPipeline(object):
    def __init__(self):
        self.es = None

    def open_spider(self, spider):
        self.es = Elasticsearch('34.192.216.218:9200')

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.es.index('news', item)
        return item


class MongoDBPipeline(object):
    def __init__(self):
        self.collection_name = None
        self.mongo_uri = 'mongodb://localhost:27017/'
        self.mongo_db = 'crawl'
        self.client = None
        self.db = None
        self.collection = None

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db['24h']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        return item


class PySolrQuotesPipeline(object):
    def open_spider(self, spider):
        self.solr = pysolr.Solr(
            'http://localhost:8983/solr/nhom1-quotes', always_commit=True)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.solr.add(
            {'text': f'{item["content"]} {item["author"]} {" ".join(item["tags"])}'})
        return item


class PySolrAuthorsPipeline(object):
    def open_spider(self, spider):
        self.solr = pysolr.Solr(
            'http://localhost:8983/solr/nhom1-authors', always_commit=True)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.solr.add(
            {'text': f'{item["name"]} {item["born_date"]} {item["born_location"]} {item["description"]}'})
        return item

# class Pipeline(object):
#     def __init__(self):
#         pass

#     def open_spider(self, spider):
#         pass

#     def close_spider(self, spider):
#         pass

#     def process_item(self, item, spider):
#         pass
