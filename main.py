import cv2
import numpy as np
from keras.models import load_model

imgpath = 'faces\with faces\easy_11_1111.jpg'


# Load the saved model
model = load_model('face_detection.model')

# Load the image you want to test
image = cv2.imread(imgpath)

# Preprocess the image to match the input shape of the model
resized_image = cv2.resize(image, (150, 150))
normalized_image = resized_image.astype('float32') / 255.0
input_image = np.expand_dims(normalized_image, axis=0)

# Predict the class of the image
prediction = model.predict(input_image)[0]

# Set a threshold probability score to decide whether the image is a face or not
threshold = 0.5
if prediction >= threshold:
    print('The image is a face!')
else:
    print('The image is not a face.')
