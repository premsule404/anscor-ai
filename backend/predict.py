from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os

# ======================
# FLASK APP
# ======================

app = Flask(__name__)
CORS(app)

# ======================
# UPLOAD FOLDER
# ======================

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):

    os.makedirs(UPLOAD_FOLDER)

# ======================
# PREDICT API
# ======================

@app.route("/predict", methods=["POST"])

def predict_anemia():

    try:

        # ======================
        # CHECK IMAGE
        # ======================

        if "image" not in request.files:

            return jsonify({

                "prediction": {

                    "result":
                        "No image uploaded",

                    "confidence":
                        "0%",

                    "hemoglobin":
                        "0 g/dL"
                }

            }), 400

        file = request.files["image"]

        # ======================
        # EMPTY FILE
        # ======================

        if file.filename == "":

            return jsonify({

                "prediction": {

                    "result":
                        "No file selected",

                    "confidence":
                        "0%",

                    "hemoglobin":
                        "0 g/dL"
                }

            }), 400

        # ======================
        # SAVE IMAGE
        # ======================

        filepath = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        file.save(filepath)

        print("IMAGE SAVED:", filepath)

        # ======================
        # RANDOM AI OUTPUT
        # ======================

        prediction_list = [

            "No Anemia Detected",

            "Mild Anemia Detected",

            "Moderate Anemia Detected"
        ]

        result = random.choice(
            prediction_list
        )

        confidence = random.randint(
            85,
            99
        )

        hemoglobin = round(

            random.uniform(8.5, 15.5),

            1
        )

        # ======================
        # RETURN RESULT
        # ======================

        return jsonify({

            "prediction": {

                "result":
                    result,

                "confidence":
                    str(confidence) + "%",

                "hemoglobin":
                    str(hemoglobin) + " g/dL"
            }

        })

    except Exception as e:

        print("SERVER ERROR:", e)

        return jsonify({

            "prediction": {

                "result":
                    "Prediction Failed",

                "confidence":
                    "0%",

                "hemoglobin":
                    "0 g/dL"
            }

        }), 500


# ======================
# RUN SERVER
# ======================

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000
    )