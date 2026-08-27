from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Damilab API is running"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_not_found():
    client = app.test_client()

    response = client.get("/does-not-exist")

    assert response.status_code == 404
    assert response.json["error"] == "Not found"
