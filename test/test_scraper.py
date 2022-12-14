import pytest
from app.main import scraper_app
from prometheus_client import REGISTRY

@pytest.fixture()
def client():
    return scraper_app.test_client()

def test_hello_world(client):
    response = client.get("/")
    assert b"<p>Hello, World!</p>" in response.data

def test_post_happy_path(client):
    before = REGISTRY.get_sample_value('http_get_total', {'url': "https://www.phaidra.ai", 'code': '200'}) or 0
    response = client.post("/", json={
        "url": "https://www.phaidra.ai"
    })
    after = REGISTRY.get_sample_value('http_get_total', {'url': "https://www.phaidra.ai", 'code': '200'}) or 0
    assert response.status_code == 200
    assert 1 == after - before

def test_post_redirect(client):
    response = client.post("/", json={
        "url": "http://phaidra.ai"
    })
    assert response.status_code == 200
    assert "301" in response.text or "308" in response.text

def test_post_404(client):
    response = client.post("/", json={
        "url": "https://google.com/notfound"
    })
    assert response.status_code == 200
    assert "404" in response.text

def test_post_invalid_url(client):
    response = client.post("/", json={
        "url": "htp://phaidra.ai"
    })
    assert response.status_code == 400
