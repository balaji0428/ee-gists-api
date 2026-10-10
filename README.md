# GitHub Gists API

A simple Flask application that returns the public GitHub Gists for a given user.

## Requirements

- Python 3.12+
- Docker

## Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

The service will be available at:

```text
http://localhost:8080
```

## Running Tests

```bash
pytest -v
```

## Running with Docker

Build the image:

```bash
docker build -t ee-gists-api .
```

Run the container:

```bash
docker run -p 8080:8080 ee-gists-api
```

Verify:

```bash
curl http://localhost:8080/octocat
```

## API

### Get User Gists

```http
GET /<user>
```

Example:

```http
GET /octocat
```

Example response:

```json
[
  {
    "id": "6cad326836d38bd3a7ae",
    "description": "Hello world!",
    "url": "https://gist.github.com/octocat/6cad326836d38bd3a7ae"
  }
]
```

Error response:

```json
{
  "error": "User not found"
}
```