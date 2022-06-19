import os
from PIL import Image


cur = os.getcwd()

img_dir = os.path.join(cur, 'data/spiral/healthy')
img_list = os.listdir(img_dir)

result_dir = os.path.join(cur, 'data/spiral/healthy_output')

if not os.path.exists(result_dir):
    os.makedirs(result_dir)

for images in img_list:
    
    img_path = os.path.join(img_dir, images)
    name = os.path.splitext(images)[0]
    
    jpg_path = os.path.join(result_dir, name + '.jpg')
    
    print(name)
    print(jpg_path)
    print(img_path)
    im = Image.open(img_path)
    bg = Image.new("RGB", im.size, (255,255,255))
    bg.paste(im, im)     # if you get bad mask error uncomment the below line
    # bg.paste(im, mask=im.split()[2])   
    bg.save(jpg_path)