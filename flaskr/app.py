import os
from flask import Flask, send_from_directory, render_template, request
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')


ES_HOST = os.getenv('ES_HOST')
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['post'])
def search():
    body = request.get_json()
    client = Elasticsearch(ES_HOST)
    response = client.search(
        index='news',
        body=body,
        params={
            'size': 20
        }
    )
    return response


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


if __name__ == '__main__':
    app.run()
