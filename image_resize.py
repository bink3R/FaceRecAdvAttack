import os
from PIL import Image

image_list = os.listdir("./images")
for image in image_list:
    obj_num = image.split('_')[0]
    origin_size = Image.open(os.path.join('./images',image)).size
    target_size = Image.open(os.path.join('./adv_images',obj_num,image)).size
    jpg_img = './adv_images/'+obj_num+'/'+image
    if(origin_size == target_size):
        continue
    else:
        print(jpg_img)
        target = Image.open(os.path.join('./adv_images',obj_num,image)).resize(origin_size,Image.ANTIALIAS)
        target.save(jpg_img)