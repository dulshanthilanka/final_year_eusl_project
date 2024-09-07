import cv2
import numpy as np
import tensorflow as tf
from PIL import Image as PilImage

# Load the pre-trained model
checkpoint_path = 'C:/Users/dulsh/Documents/PROJECT_EUSL/pythonProject/model/best_model.h5'
model = tf.keras.models.load_model(checkpoint_path)

# Define emotion labels
label_to_text = {0: 'anger', 1: 'disgust', 2: 'fear', 3: 'happiness', 4: 'sadness', 5: 'surprise', 6: 'neutral'}

# Function to predict the expression for an image
def predict_expression(image):
    # Convert PIL image to NumPy array
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Assuming the image is in RGB format
    img = cv2.resize(img, (48, 48))
    img = img.reshape(1, 48, 48, 1)
    img = img / 255.0

    # Predict the expression using the model
    prediction = model.predict(img)
    expression_label = label_to_text[np.argmax(prediction)]
    return expression_label
