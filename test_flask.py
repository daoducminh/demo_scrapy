from flask import Flask, jsonify
import pysolr
import json

app = Flask(__name__)


@app.route('/book')
def demo():
    solr = pysolr.Solr('http://localhost:8983/solr/books', always_commit=True)
    docs = solr.search('title:Harry')
    result = []
    for doc in docs:
        result.append({
            'title': doc['title'],
            'authors': doc['authors']
        })
    return jsonify(result)


@app.route('/')
def test():
    solr = pysolr.Solr('http://localhost:8983/solr/test', always_commit=True)
    docs = solr.search('title:Viber')
    result = []
    for doc in docs:
        result.append({
            'title': doc['title'],
            'url': doc['url']
        })
    return jsonify(result)
