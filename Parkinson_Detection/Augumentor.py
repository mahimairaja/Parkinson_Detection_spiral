# Use this as a boiler plater if you want to augument the datas simply

cur_dir = os.getcwd() 

data = ImageDataGenerator(
                rotation_range= 40,
                width_shift_range= 0.2,
                height_shift_range= 0.2,
                shear_range= 0.2,
                zoom_range= 0.2,
                horizontal_flip= True,
                fill_mode = 'nearest'
)

img_path = os.path.join(cur_dir,'data/spiral/healthy')
img_list = os.listdir(img_path)

print(img_list)

augumented_folder = os.path.join(cur_dir,'data/augumented/train/healthy')

if not os.path.exists(augumented_folder):
    os.makedirs(augumented_folder)

for images in img_list:
    name = os.path.splitext(images)[0]

    cur_img_path = os.path.join('data/spiral/healthy',images)


    img = load_img(cur_img_path)
    img_array = img_to_array(img)
    img_array = img_array.reshape((1,) + img_array.shape)

    augumented_train_images = 1

    augumented_trainH = os.path.join(cur_dir, 'data/augumented/train/healthy')
    if not os.path.exists(augumented_train):
        os.makedirs(augumented_train)


    for batch in data.flow(img_array, batch_size=1, save_to_dir= augumented_trainH, save_prefix=name, save_format='png'):
                            augumented_train_images += 1
                            if augumented_train_images > 2 :
                                break