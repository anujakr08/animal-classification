# Animal Classification Using CNN and Flask

This project implements a **Convolutional Neural Network (CNN)** to classify animals, deployed as a web application using **Flask**. Users can upload an image of an animal, and the model predicts whether the image is of a **Cat**, **Dog**, or **Fox**. If the image is not recognized, the app will notify the user. Additionally, the application is capable of detecting human faces and will inform the user if the uploaded image is of a human.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Screenshots](#screenshots)


## Overview

This project is designed to classify images of animals into three categories: **Cat**, **Dog**, or **Fox**. The backend is built using Flask, and the model is a trained CNN. The frontend is simple and intuitive, allowing users to upload images and get real-time predictions from the model.

If the image contains a human face, the application will return a message saying, "This is a human, not an animal."

## Features

- Upload an image through the browser.
- Display the uploaded image on the page before predicting.
- Run the image through a CNN model to classify the animal.
- Detect if the image contains a human face and return a message accordingly.
- Display a message if the animal is not recognized by the model.

## Architecture

- **Frontend**: A simple HTML page with a form to upload images.
- **Backend**: Flask server handling image uploads, running predictions using a pre-trained CNN model, and returning the results as JSON.
- **Model**: Convolutional Neural Network (CNN) trained on a dataset containing images of Cats, Dogs, and Foxes.

## Requirements

- Python 3.x
- Flask
- TensorFlow/Keras (for CNN model)
- OpenCV (for face detection)
- Pillow (for image processing)

### Installation of Dependencies

You can install the required Python packages by running:

```bash
pip install -r requirements.txt
git clone https://github.com/your-username/animal-classification-cnn.git
cd animal-classification-cnn
python app.py
Open your browser and go to http://127.0.0.1:5000/ to view and use the application.
```
## Usage

**How to Use the Application:**
Open the web application in your browser.
Upload an image using the "Choose File" button.
Click "Submit" to upload the image.
The uploaded image will be displayed on the page, and the predicted animal will be shown below the image.
If the image is not recognized or contains a human face, a corresponding message will be displayed.

## Screenshots
![image](https://github.com/user-attachments/assets/7d3a9701-29bc-4040-980a-4a305893d6ac)
![image](https://github.com/user-attachments/assets/d4d26f4f-4327-4956-8c2a-7b1753b38569)
![image](https://github.com/user-attachments/assets/c432a9dd-0af6-4eed-95d9-cbbc0ce2a568)


