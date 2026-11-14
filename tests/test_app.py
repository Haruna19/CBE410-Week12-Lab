from app import app

def test_health():
    with app.test_client() as client:
        response = client.get('/health')

        assert response.status_code == 201
        assert response.json == {'status': 'ok'}

def test_greet_limit():
    with app.test_client() as client:
        assert client.get('/greet?name=' + 'a'*60).json['message'] == 'Hello, ' + 'a'*40 + '!'
