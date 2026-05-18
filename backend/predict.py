import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# LOAD MODEL
model = tf.keras.models.load_model("models/resnet50_model.h5")

def predict_anemia(img_path):

    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        result = "Anemic"
        hb = "8-10 g/dL"
    else:
        result = "Healthy"
        hb = "12-15 g/dL"

    confidence = round(float(prediction) * 100, 2)

    return {
        "result": result,
        "confidence": confidence,
        "hemoglobin": hb
    }