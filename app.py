from flask import Flask, request, jsonify, render_template
from model import predict_animal
from PIL import Image
import io
import base64
import cv2
import numpy as np

app = Flask(__name__)

# Define the animal classes
animal_classes = ["Cat", "Dog", "Fox"]

def detect_human_face(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return len(faces) > 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    img = Image.open(io.BytesIO(file.read()))

    # Convert the image to base64 to render on the web page
    img_io = io.BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.read()).decode('ascii')

    # Check if the image contains a human face
    if detect_human_face(img):
        return jsonify({'prediction': 'This is a human, not an animal', 'image': img_base64})

    # Run the animal prediction if no human face is detected
    predicted_class_idx = predict_animal(img)

    if predicted_class_idx is None:
        predicted_animal = "That image is not in the model"
    else:
        predicted_animal = animal_classes[predicted_class_idx]

    return jsonify({'prediction': predicted_animal, 'image': img_base64})

if __name__ == '__main__':
    app.run(debug=True)
