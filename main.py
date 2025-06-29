from flask import Flask, send_file, jsonify
import json

app = Flask(__name__)

@app.route("/version.json")
def serve_version():
    with open("version.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/firmware/<filename>")
def serve_firmware(filename):
    path = f"firmwares/{filename}"
    return send_file(path)

@app.route("/")
def hello():
    return "🚀 OTA Server is running!"

if __name__ == "__main__":
    app.run()
