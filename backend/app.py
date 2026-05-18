from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

from predict import predict_anemia

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory("../", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("../", path)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['image']

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(filepath)

    result = predict_anemia(filepath)

    return jsonify({
    "prediction": result
})

if __name__ == "__main__":
    app.run(debug=True)