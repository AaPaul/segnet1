import numpy as np
import matplotlib
import os
from PIL import Image

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def img_seg(dir):
    files = os.listdir(dir)
    for file in files:
        a, b = os.path.splitext(file)
        img = Image.open(os.path.join(dir + "\\" + file))
        hight, width = img.size
        w = 480
        id = 1
        i = 0
        while (i + w <= hight):
            j = 0

            while (j + w <= width):
                new_img = img.crop((i, j, i + w, j + w))
                # rename = "D:\\labelme\\images\\"
                rename = "D:\\segnet\\data_set\\train_test\\"
                new_img.save(rename + a + "_" + str(id) + b)
                id += 1
                j += w
            i = i + w


if __name__ == '__main__':
    # path = "D:\\labelme\\data\\images\\train"
    path = "D:\\segnet\\data_set\\train"
    img_seg(path)