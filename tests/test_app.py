import pytest
from app import create_app

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_generator_page(client):
    response = client.get('/generator')
    assert response.status_code == 200

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_404(client):
    response = client.get('/404-does-not-exist')
    assert response.status_code == 404

@pytest.fixture
def app():
    app = create_app()
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
