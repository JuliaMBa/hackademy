import os
from PIL import Image

def rotate_box(an_image): 
    box =(100,100,400,400)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed,box)
    return an_image

def get_filenames(a_dirname):
    list_of_files = os.listdir(a_dirname)
    all_files = []
    for filename in list_of_files:
        full_path = os.path.join(a_dirname,filename)
        if not os.path.isdir(full_path):
            all_files.append(full_path)
    return all_files

    #print
pic_list = get_filenames("C:\\Users\\JuliaMB\\Desktop\\Pictures")
for pic_name in pic_list:
    im = Image.open(pic_name)
    im = rotate_box(im)
    im.save("C:\\Users\\JuliaMB\\Desktop\\Pictures\\picture2.jpg")


# solution transform pictures by rotation, save them in different folder

