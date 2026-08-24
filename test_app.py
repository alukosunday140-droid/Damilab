import pytest
from app import app

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"DamiLab" in response.data  # checks if "DamiLab" is on page

def test_about_page():
    client = app.test_client()
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About" in response.data
