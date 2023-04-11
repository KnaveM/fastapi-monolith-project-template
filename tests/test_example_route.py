# tests/test_example_route.py
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_example_route():
    response = client.get("/example")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, this is an example route!"}
