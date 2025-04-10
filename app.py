# from flask import Flask, request, jsonify, render_template
# import os
# from flask_cors import CORS, cross_origin
# from KidneydiseaseClassifier.utils.common import decodeImage
# from KidneydiseaseClassifier.pipeline.prediction import PredictionPipeline



# os.putenv('LANG', 'en_US.UTF-8')
# os.putenv('LC_ALL', 'en_US.UTF-8')

# app = Flask(__name__)
# CORS(app)


# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
#         self.classifier = PredictionPipeline(self.filename)


# @app.route("/", methods=['GET'])
# @cross_origin()
# def home():
#     return render_template('index.html')




# @app.route("/train", methods=['GET','POST'])
# @cross_origin()
# def trainRoute():
#     os.system("python main.py")
#     # os.system("dvc repro")
#     return "Training done successfully!"



# @app.route("/predict", methods=['POST'])
# @cross_origin()
# def predictRoute():
#     image = request.json['image']
#     decodeImage(image, clApp.filename)
#     result = clApp.classifier.predict()
#     return jsonify(result)


# if __name__ == "__main__":
#     clApp = ClientApp()

#     app.run(host='0.0.0.0', port=8080) #for AWS

from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from KidneydiseaseClassifier.utils.common import decodeImage
from KidneydiseaseClassifier.pipeline.prediction import PredictionPipeline

# Set encoding environment
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

# Client wrapper class
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Home route
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

# Training route
@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"

# Prediction route for base64 input from frontend
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()  # This should return a dict, like {"prediction": "Tumor", "confidence": 0.98}
    return jsonify(result)


# App start
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)
