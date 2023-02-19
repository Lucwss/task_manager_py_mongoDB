from fastapi.testclient import TestClient

from .application import app

client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'welcome to my personal project'}


