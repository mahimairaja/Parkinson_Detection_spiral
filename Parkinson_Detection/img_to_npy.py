import os
from PIL import Image
from numpy import asarray
from numpy import save

cur = os.getcwd()

img_dir = os.path.join(cur, 'healthy')  # Original Image directory 
np_dir = os.path.join(cur, 'numpy')     # Directory where numpy files to be saved
img_list = os.listdir(img_dir)

if not os.path.exists(np_dir):
    os.makedirs(np_dir)

for images in img_list:
    name = os.path.splitext(images)[0]

    cur_img_path = os.path.join('healthy',images)

    img = Image.open(cur_img_path)
    np_array = asarray(img)
    
    save(os.path.join(np_dir, images+'.npy'), np_array)
    print(np_array)


