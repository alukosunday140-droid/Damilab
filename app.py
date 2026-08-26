import pytest
import sys
import os

# This makes sure pytest can find app.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # turns off forms CSRF for testing
    with app.test_client() as client:
        yield client

def test_home_page_loads(client):
    """Test that homepage returns 200 OK"""
    response = client.get('/')
    assert response.status_code == 200

def test_dummy():
    assert True
