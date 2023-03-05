import cv2
import numpy as np
from keras.models import load_model

def detect_face(imgpath):

    # Load the Cascade Classifier for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Load the image to be processed
    img = cv2.imread(imgpath)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image using Cascade Classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If no faces are detected, print a message
    if len(faces) == 0:
        return False
    else:
        # If faces are detected, print a message
        return True 
