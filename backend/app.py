from flask import (
    Flask,
    request,
    jsonify,
    send_from_directory
)

from flask_cors import CORS

import os

from predict import predict_anemia


# ======================
# FLASK APP
# ======================

app = Flask(__name__)

CORS(app)


# ======================
# FRONTEND ROUTES
# ======================

@app.route("/")
def home():

    return send_from_directory(
        "../",
        "index.html"
    )


@app.route("/<path:path>")
def static_files(path):

    return send_from_directory(
        "../",
        path
    )


# ======================
# UPLOAD FOLDER
# ======================

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):

    os.makedirs(UPLOAD_FOLDER)


# ======================
# PREDICTION ROUTE
# ======================

@app.route(
    "/predict",
    methods=["POST"]
)

def predict():

    try:

        # CHECK IMAGE

        if "image" not in request.files:

            return jsonify({
                "result":
                "No image uploaded"
            }), 400

        file = request.files["image"]
           

        # CHECK EMPTY FILE

        if file.filename == "":

            return jsonify({
                "result":
                "No selected file"
            }), 400

        # SAVE IMAGE

        filepath =os.path.join(
            
                UPLOAD_FOLDER,
                file.filename
            )

        file.save(filepath)

        # PREDICT

        prediction_data = predict_anemia(filepath)
           

        print(prediction_data)

        # RETURN RESULT

        return jsonify({

            "result":
                prediction_data["result"],

            "confidence":
                prediction_data["confidence"],

            "hemoglobin":
                prediction_data["hemoglobin"]

        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({

            "result":
                "Prediction Failed",

            "confidence":
                "0%",

            "hemoglobin":
                "0 g/dL"

        }), 500


# ======================
# RUN APP
# ======================

if __name__ == "__main__":

    app.run(
        debug=True
    )