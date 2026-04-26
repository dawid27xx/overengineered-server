from __future__ import annotations

from typing import Any

from flask import Flask, request

app: Flask = Flask(__name__)


@app.route('/sampleGet')
def sampleGet() -> str:
    return 'Hello, World!'


@app.route('/sampleGet2')
def sampleGet2() -> str:
    return 'Hello, World2!'


@app.route('/sampleGet3')
def sampleGet3() -> str:
    return 'Hello, World3!'


@app.route('/samplePost', methods=['POST'])
def samplePost() -> dict[str, Any]:
    req: Any = request.get_json()
    return {'received': req}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
