import pytest
from app import app, db, User
from unittest.mock import patch
import json
import io

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/salud')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'ok'

@patch('app.analizar_imagen')
@patch('app.obtener_imagen_especie')
def test_analizar_endpoint(mock_image_search, mock_analizar, client):
    """Test the image analysis endpoint."""
    mock_analizar.return_value = {
        "nombre": "Chinita",
        "cientifico": "Harmonia axyridis",
        "descripcion": "Un insecto pequeño y manchado.",
        "habitat": "Todo Chile",
        "peligrosidad": "Baja",
        "estado_conservacion": "Preocupación Menor",
        "puntos": 20,
        "tipo": "insecto"
    }
    mock_image_search.return_value = "http://example.com/chinita.jpg"

    data = {
        'imagen': (io.BytesIO(b"fake image data"), 'test.jpg'),
        'tipo': 'insecto'
    }
    response = client.post('/analizar', data=data, content_type='multipart/form-data')
    
    assert response.status_code == 200
    res_data = json.loads(response.data)
    assert res_data['nombre'] == "Chinita"
    assert res_data['estado_conservacion'] == "Preocupación Menor"
    assert res_data['imagen_url'] == "http://example.com/chinita.jpg"

@patch('app.buscar_por_texto')
@patch('app.obtener_imagen_especie')
def test_buscar_endpoint(mock_image_search, mock_buscar, client):
    """Test the text search endpoint."""
    mock_buscar.return_value = {
        "nombre": "Copihue",
        "cientifico": "Lapageria rosea",
        "descripcion": "La flor nacional de Chile.",
        "habitat": "Sur de Chile",
        "peligrosidad": "Baja",
        "estado_conservacion": "Vulnerable",
        "puntos": 80,
        "tipo": "planta"
    }
    mock_image_search.return_value = "http://example.com/copihue.jpg"

    response = client.post('/buscar', 
                           data=json.dumps({'consulta': 'Copihue', 'tipo': 'planta'}),
                           content_type='application/json')
    
    assert response.status_code == 200
    res_data = json.loads(response.data)
    assert res_data['nombre'] == "Copihue"
    assert res_data['estado_conservacion'] == "Vulnerable"
    assert res_data['imagen_url'] == "http://example.com/copihue.jpg"
