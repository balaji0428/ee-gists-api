from unittest.mock import patch
from app import app

client = app.test_client()

@patch('app.requests.get')
def test_get_gists_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "id": "1",
            "description": "Test Gist",
            "html_url": "https://gist.github.com/1"
        }
    ]

    response = client.get('/testuser')
    assert response.status_code == 200
    assert response.json == [
        {
            "id": "1",
            "description": "Test Gist",
            "url": "https://gist.github.com/1"
        }
    ]
    response = client.get('/octocat')
    assert response.status_code == 200
    data = response.get_json()
    assert data[0]['id'] == '1'
    assert data[0]['description'] == 'Test Gist'
    
@patch('app.requests.get')
def test_get_gists_user_not_found(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    response = client.get('/nonexistentuser')
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}