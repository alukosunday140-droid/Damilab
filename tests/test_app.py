import pytest

from app import create_app
from app.config import TestingConfig


@pytest.fixture()
def app():
    app = create_app(TestingConfig)
    app.config["PROPAGATE_EXCEPTIONS"] = False

    @app.route("/test-error")
    def test_error():
        raise Exception("Test error")

    return app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.is_json
    assert response.json["message"] == "Damilab API is running"
    assert response.json["version"] == "1.0.0"


def test_health(client):def test_courses(client):
    response = client.get("/api/courses")

    assert response.status_code == 200
    assert response.is_json
    assert "courses" in response.json
    assert len(response.json["courses"]) == 3
    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.json["status"] == "ok"


def test_not_found(client):
    response = client.get("/does-not-exist")

    assert response.status_code == 404
    assert response.is_json
    assert response.json["error"] == "Not found"


def test_internal_server_error(client):
    response = client.get("/test-error")

    assert response.status_code == 500
    assert response.is_json
    assert response.json["error"] == "Internal server error"
