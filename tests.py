import pytest
from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_sample_get(client):
    response = client.get('/sampleGet')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello, World!'


def test_sample_post(client):
    response = client.post('/samplePost', json={'key': 'value'})
    assert response.status_code == 200
    assert response.get_json() == {'received': {'key': 'value'}}
