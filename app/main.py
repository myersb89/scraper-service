import requests
import sys
from flask import Flask, request
from prometheus_client import generate_latest, Counter, start_http_server

app = Flask(__name__)
http_get_counter = Counter('http_get', 'HTTP GETS performed', ['url','code'])
start_http_server(9095)

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/")
def scraper_service():

    data = request.get_json()
    # TODO input validation
    url = data.get('url')
    #print(f'url is {url}', file=sys.stderr)

    r = requests.get(url)
    http_get_counter.labels(url=url, code=r.status_code).inc()

    return f"<p>HTTP response code from {url} is {r.status_code}</p>"

