GitHub Gists API
A simple HTTP web service that returns the publicly available GitHub Gists for a given user.
The solution intentionally keeps the implementation minimal and focused on the requirements. It exposes a single endpoint that retrieves public gists from the GitHub API and returns them to the caller.
Prerequisites
* Python 3.12+
* Docker (optional)
Project Structure
```text
.
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── tests
└── test_app.py
```
Running Locally
1. Install Dependencies
```bash
pip install -r requirements.txt
```
2. Start the Application
```bash
python app.py
```
The application will start on:
```text
http://localhost:8080
```
Example Request
```bash
curl http://localhost:8080/octocat
```
Example Response
```json
[
{
"id": "example-id",
"description": "Example gist",
"html_url": "https://gist.github.com/example"
}
]
```
Running Tests
Execute:
```bash
pytest
```
The automated test validates that the API successfully returns publicly available gists for the example GitHub user:
```text
octocat
```
Docker
Build Image
```bash
docker build -t github-gists-api .
```
Run Container
```bash
docker run -p 8080:8080 github-gists-api
```
The service will be available at:
```text
http://localhost:8080
```
Verify
```bash
curl http://localhost:8080/octocat
```
Endpoint
Get User Gists
```http
GET /<USER>
```
Example:
```http
GET /octocat
```
Returns the user's publicly available GitHub Gists.
Notes
This implementation satisfies the required functionality:
* HTTP endpoint at `/<USER>`
* Retrieves public gists from the GitHub API
* Automated test included
* Dockerized application
* Container listens on port `8080`
Potential future enhancements such as pagination, caching, authentication, and rate-limit handling have been intentionally omitted to keep the solution simple, clear, and maintainable.


