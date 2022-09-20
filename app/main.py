import requests
import sys
from flask import Flask, request
from prometheus_client import generate_latest, Counter

app = Flask(__name__)
http_get_counter = Counter('http_get', 'HTTP GETS performed', ['url','code'])

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

@app.route('/metrics')
def metrics():
    return generate_latest()
