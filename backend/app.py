from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    print("Image saved at:", filepath)

    # TEMP FAKE OUTPUT (for testing)
    result = "No Anemia Detected (Demo)"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)