import requests
import sys
import validators
from flask import Flask, request
from prometheus_client import generate_latest, Counter, start_http_server, REGISTRY

scraper_app = Flask(__name__)
http_get_counter = Counter('http_get', 'HTTP GETS performed', ['url','code'])
start_http_server(9095)

@scraper_app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@scraper_app.post("/")
def scraper_service():

    data = request.get_json()
    url = data.get('url')

    if validators.url(url):
        r = requests.get(url, allow_redirects=False)
        http_get_counter.labels(url=url, code=r.status_code).inc()
        return f"<p>HTTP response code from {url} is {r.status_code}</p>", 200
    else:
        return "Invalid URL", 400

