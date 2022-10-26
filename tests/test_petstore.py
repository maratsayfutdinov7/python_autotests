import requests
import pytest

def test_statuscode():
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{788}')
    assert response.status_code == 200

def test_body_name():
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{788}')
    assert response.json()["name"] == "Jasmina"