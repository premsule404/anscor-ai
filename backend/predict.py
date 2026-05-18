import tensorflow as tf

import numpy as np

from tensorflow.keras.preprocessing import image

import os


# ======================
# LOAD MODEL
# ======================

MODEL_PATH ="models/resnet50_model.h5"

    
model =tf.keras.models.load_model(
    
        MODEL_PATH
    )


# ======================
# PREDICT FUNCTION
# ======================

def predict_anemia(img_path):

    try:

        # CHECK FILE

        if not os.path.exists(img_path):

            return {

                "result":
                    "Image Not Found",

                "confidence":
                    "0%",

                "hemoglobin":
                    "0 g/dL"
            }

        # LOAD IMAGE

        img = image.load_img(
           
                img_path,
                target_size=(224, 224)
            )

        # CONVERT IMAGE

        img_array = image.img_to_array(img)

           
        # RESHAPE

        img_array = np.expand_dims(
           
                img_array,
                axis=0
            )

        # NORMALIZE

        img_array =img_array / 255.0
            

        # MODEL PREDICTION

        prediction = model.predict(
           
                img_array
            )[0][0]

        print("RAW PREDICTION:",
              prediction)

        # ======================
        # CLASSIFICATION
        # ======================

        if prediction > 0.5:

            result ="Potential Anemia Detected"
                

            hb =  "8-10 g/dL"
              

            confidence =round(
                
                    float(prediction) * 100,
                    2
                )

        else:

            result ="No Anemia Detected"
                

            hb =  "12-15 g/dL"
              

            confidence = round(
               
                    (1 - float(prediction)) * 100,
                    2
                )

        # ======================
        # RETURN RESULT
        # ======================

        return {

            "result":
                result,

            "confidence":
                str(confidence) + "%",

            "hemoglobin":
                hb
        }

    except Exception as e:

        print("PREDICTION ERROR:", e)

        return {

            "result":
                "Prediction Failed",

            "confidence":
                "0%",

            "hemoglobin":
                "0 g/dL"
        }