"""
Unit tests for Calculator API
"""

import pytest
from app import app

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == 'Calculator API'

def test_add_endpoint(client):
    """Test addition endpoint"""
    response = client.post('/add', json={'a': 5, 'b': 3})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8
    assert data['operation'] == 'addition'

def test_subtract_endpoint(client):
    """Test subtraction endpoint"""
    response = client.post('/subtract', json={'a': 10, 'b': 4})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 6
    assert data['operation'] == 'subtraction'

def test_multiply_endpoint(client):
    """Test multiplication endpoint"""
    response = client.post('/multiply', json={'a': 6, 'b': 7})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 42
    assert data['operation'] == 'multiplication'

def test_divide_endpoint(client):
    """Test division endpoint"""
    response = client.post('/divide', json={'a': 20, 'b': 4})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 5
    assert data['operation'] == 'division'

def test_divide_by_zero(client):
    """Test division by zero error handling"""
    response = client.post('/divide', json={'a': 10, 'b': 0})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_invalid_input(client):
    """Test invalid input handling"""
    response = client.post('/add', json={'a': 'invalid', 'b': 5})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_missing_parameters(client):
    """Test missing parameters"""
    response = client.post('/add', json={})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 0

