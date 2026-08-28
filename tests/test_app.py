from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.is_json
    assert response.json["message"] == "Damilab API is running"
    assert response.json["version"] == "1.0.0"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.json["status"] == "ok"


def test_not_found():
    client = app.test_client()

    response = client.get("/does-not-exist")

    assert response.status_code == 404
    assert response.is_json
    assert response.json["error"] == "Not found"


def test_internal_server_error():
    client = app.test_client()

    @app.route("/test-error")
    def test_error():
        raise Exception("Test error")

    app.config["TESTING"] = False

    response = client.get("/test-error")

    assert response.status_code == 500
    assert response.is_json
    assert response.json["error"] == "Internal server error"
