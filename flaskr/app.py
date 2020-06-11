import os
from flask import Flask, send_from_directory, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['post'])
def search():
    body = request.get_json()
    client = Elasticsearch('23.98.73.116:9200')
    response = client.search(
        index='news',
        body=body
    )
    return response


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


if __name__ == '__main__':
    app.run()
