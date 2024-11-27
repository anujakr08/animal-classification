from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Load your model
model = load_model('animal.h5')

# Function to predict
CONFIDENCE_THRESHOLD = 0.6

def predict_animal(image):
    # Preprocess the image for your model
    image = image.resize((256, 256))  # Adjust the size according to your model input
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    # Predict the class probabilities
    predictions = model.predict(image)

    # Get the index of the highest probability class
    predicted_class_idx = np.argmax(predictions, axis=1)[0]  # Get the index
    confidence = np.max(predictions, axis=1)[0]  # Get the confidence (highest probability)

    # Check if the confidence is above the threshold
    if confidence < CONFIDENCE_THRESHOLD:
        return None  # Confidence is too low, return None

    return predicted_class_idx  # Return the class index if confidence is sufficient
