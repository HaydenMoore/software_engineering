import requests
import json

def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_weather_basic():
    response = requests.get("https://www.metaweather.com/api/location/search/?query=london")
    assert response
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    result = json.loads(response.text)
    assert type(result) is list
    assert len(result) == 1
    data = result[0]
    assert type(data) is dict
    assert data['title'] == "London"

