from flask import Flask, jsonify  # type: ignore

app = Flask(__name__)


@app.route("/")
def read_root():
    return jsonify({"message": "Hello, World!"})
