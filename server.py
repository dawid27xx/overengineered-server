from flask import Flask, request

app = Flask(__name__)


@app.route('/sampleGet')
def sampleGet():
    return 'Hello, World!'


@app.route('/samplePost', methods=['POST'])
def samplePost():
    req = request.get_json()
    return {'received': req}






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
