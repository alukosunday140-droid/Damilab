
    import pytest
    from app import app  # This imports YOUR flask app

    @pytest.fixture
    def client():
        """Creates a test client for the app"""
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    def test_home_page_loads(client):
        """Test that homepage returns 200 OK"""
        response = client.get('/')
        assert response.status_code == 200

    def test_math_still_works():
        """Keep dummy test so CI doesn't break"""
        assert 2 + 2 == 4
