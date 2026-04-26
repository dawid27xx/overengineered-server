import pytest
from collections.abc import Generator
from flask.testing import FlaskClient

from server import app


@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    with app.test_client() as client:
        yield client


def test_sample_get(client: FlaskClient) -> None:
    response = client.get('/sampleGet')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello, World!'


def test_sample_get2(client: FlaskClient) -> None:
    response = client.get('/sampleGet2')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello, World2!'


def test_sample_get3(client: FlaskClient) -> None:
    response = client.get('/sampleGet3')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello, World3!'


def test_sample_post(client: FlaskClient) -> None:
    response = client.post('/samplePost', json={'key': 'value'})
    assert response.status_code == 200
    assert response.get_json() == {'received': {'key': 'value'}}
