import os 
import cv2 as cv

cur = os.getcwd()
img_dir = os.path.join(cur, 'data/spiral/healthy')
img_list = os.listdir(img_dir)

rgb_dir = os.path.join(cur, 'data/rgb/healthy')

if not os.path.exists(rgb_dir):
    os.makedirs(rgb_dir)

for images in img_list:
    name = os.path.splitext(images)[0]
    
    cur_img_path = os.path.join(img_dir,images)
    print(cur_img_path)
    
    gray = cv.imread(cur_img_path)
    rgb = cv.cvtColor(gray, cv.COLOR_GRAY2RGB)
    
    save_path = os.path.join(rgb_dir,name+'.png')
    cv.imwrite(save_path, rgb)
    