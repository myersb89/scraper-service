import requests
import argparse
import random
from time import sleep


parser = argparse.ArgumentParser()
parser.add_argument("port", nargs='?', type=int, default=31534, help="Override the localhost port")
args = parser.parse_args()

urls = ["http://phaidra.ai", "https://phaidra.ai", "https://www.phaidra.ai", "https://google.com"]

# Keep generating traffic until we quit
while True:

    url = urls[random.randint(0, len(urls)-1)]
    print(f"Scraping {url}...")
    r = requests.post(f'http://localhost:{args.port}', json = {"url": url})
    print(f"Status code: {r.status_code}")
    sleep(random.randint(1, 5))