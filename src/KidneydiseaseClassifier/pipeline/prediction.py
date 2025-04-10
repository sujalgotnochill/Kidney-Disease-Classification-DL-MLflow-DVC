from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.model = load_model(os.path.join("artifacts", "training", "model.h5"))

    def predict(self):
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image) / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        preds = self.model.predict(test_image)
        predicted_index = np.argmax(preds, axis=1)[0]
        confidence = np.max(preds)

        class_map = {0: 'Normal', 1: 'Tumor'}
        prediction = class_map[predicted_index]

        print(f"Predicted: {prediction} | Confidence: {confidence:.2f}")

        return [{"image": prediction, "confidence": float(confidence)}]
