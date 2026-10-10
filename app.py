from flask import Flask, jsonify
import requests

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users/"


@app.route('/<user>')
def get_gists(user):
    try:
        response = requests.get(
            f"{GITHUB_API_URL}{user}/gists",
            timeout=5
        )
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 503

    if response.status_code == 404:
        return jsonify({"error": "User not found"}), 404

    gists = response.json()

    result = [
        {
            "id": gist["id"],
            "description": gist.get("description"),
            "url": gist["html_url"]
        }
        for gist in gists
    ]

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)