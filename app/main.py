import requests
import sys
from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/")
def scraper_service():

    data = request.get_json()
    url = data.get('url')
    #print(f'url is {url}', file=sys.stderr)

    r = requests.get(url)

    return f"<p>HTTP response code from {url} is {r.status_code}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)