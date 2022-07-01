import cv2 
import pyfiglet
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import load_model, model_from_json

cur_dir = os.getcwd()
img_path = ('/Users/mahimairaja/Desktop/tri.png')

json_file = open('models/model2/model_structure.json','r')
model_structure = json_file.read()
json_file.close()

model = model_from_json(model_structure)

model.load_weights('models/model2/model_weights.h5')

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cascade = cv2.CascadeClassifier('cascade.xml')

frame = img
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

spiral_box = cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=100,
    minSize=(50, 50),
    flags=cv2.CASCADE_SCALE_IMAGE )

for (x, y, w, h) in spiral_box:
    cv2.rectangle(frame, 
                  (x-w, y-h), 
                  (x+2*w,y+2*h), 
                  (0, 255, 0),  
                   20)

    
    plt.imshow(frame)
print(len(spiral_box))

if spiral_box.all() == True :

    