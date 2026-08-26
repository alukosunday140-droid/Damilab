
    from app import app

    def test_home_page_loads():
        """Test that homepage returns 200 OK"""
        app.config['TESTING'] = True
        client = app.test_client()
        response = client.get('/')
        assert response.status_code == 200

    def test_dummy():
        assert True
