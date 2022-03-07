import pytest
import requests

def test_status_code_200():
    url = 'http://localhost:8080/swagger/'
    assert requests.get(url).status_code == 200