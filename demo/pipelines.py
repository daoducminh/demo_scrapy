# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json
import os
import pickle

from elasticsearch import Elasticsearch
from scrapy.exceptions import DropItem

# import pysolr

URLS_FILE = os.getenv('URLS_FILE')
ES_HOST = os.getenv('ES_HOST')
ES_INDEX = os.getenv('ES_INDEX')


class RemoveDuplicatedPipeline(object):
    def open_spider(self, spider):
        try:
            with open(URLS_FILE, 'rb') as file:
                self.urls = pickle.load(file)
        except Exception:
            self.urls = []

    def close_spider(self, spider):
        with open(URLS_FILE, 'wb') as file:
            pickle.dump(self.urls, file)

    def process_item(self, item, spider):
        url = item['url']
        if url in self.urls:
            raise DropItem('Duplicated item found:', item)
        else:
            self.urls.append(url)
            return item


class JsonQuotesWriterPipeline(object):
    def open_spider(self, spider):
        self.file_quotes = open('quotes.json', 'w')
        self.file_quotes.write('[\n')
        self.file_authors = open('authors.json', 'w')
        self.file_authors.write('[\n')

    def close_spider(self, spider):
        self.file_quotes.write(']')
        self.file_quotes.close()
        self.file_authors.write(']')
        self.file_authors.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item))+',\n'
        if 'content' in item:
            self.file_quotes.write(line)
        else:
            self.file_authors.write(line)
        return item


class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('test.json', 'w')
        self.file.write('[\n')

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        if item:
            line = json.dumps(dict(item))+',\n'
            self.file.write(line)
        return item


class ElasticSearchPipeline(object):
    def __init__(self):
        self.es = None

    def open_spider(self, spider):
        self.es = Elasticsearch(ES_HOST)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.es.index(ES_INDEX, item)
        return item


# class MongoDBPipeline(object):
#     def __init__(self):
#         self.collection_name = None
#         self.mongo_uri = 'mongodb://localhost:27017/'
#         self.mongo_db = 'crawl'
#         self.client = None
#         self.db = None
#         self.collection = None

#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#         self.collection = self.db['24h']

#     def close_spider(self, spider):
#         self.client.close()

#     def process_item(self, item, spider):
#         self.collection.insert_one(item)
#         return item


# class PySolrQuotesPipeline(object):
#     def open_spider(self, spider):
#         self.solr = pysolr.Solr(
#             'http://localhost:8983/solr/nhom1-quotes', always_commit=True)

#     def close_spider(self, spider):
#         pass

#     def process_item(self, item, spider):
#         self.solr.add(
#             {'text': f'{item["content"]} {item["author"]} {" ".join(item["tags"])}'})
#         return item


# class PySolrAuthorsPipeline(object):
#     def open_spider(self, spider):
#         self.solr = pysolr.Solr(
#             'http://localhost:8983/solr/nhom1-authors', always_commit=True)

#     def close_spider(self, spider):
#         pass

#     def process_item(self, item, spider):
#         self.solr.add(
#             {'text': f'{item["name"]} {item["born_date"]} {item["born_location"]} {item["description"]}'})
#         return item

# class Pipeline(object):
#     def __init__(self):
#         pass

#     def open_spider(self, spider):
#         pass

#     def close_spider(self, spider):
#         pass

#     def process_item(self, item, spider):
#         pass
