# import tensorflow as tf
# from tensorflow.python.framework import ops
# from tensorflow.python.framework import dtypes
# import os, sys
# import numpy as np
# import math
# import skimage
# import skimage.io


import os

from matplotlib import pyplot as plt

from PIL import Image

import cv2


'''
这里将图片集转换为视频
'''

# # im = Image.open("E:\\workspace\\mystoreroom\\segnet1\\SegNet\\CamVid\\trainannot\\0001TP_006690.png")
# im = "E:\\workspace\\mystoreroom\\segnet1\\SegNet\\CamVid\\testannot\\0001TP_008550.png"
# img = cv2.imread(im, 0)
# plt.imshow(img)
# plt.savefig("E:\\workspace\\mystoreroom\\segnet1\\SegNet\\CamVid\\testimg")
# plt.show()

# img_root = "E:\\workspace\\mystoreroom\\segnet1\\test_pic\\output\\testing_image"
img_root = "E:\\workspace\\mystoreroom\\segnet1\\SegNet\\CamVid\\new\\"
fps = 5
# size = (width, height)
size = (480, 360)
videowriter = cv2.VideoWriter("BB.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)

# for i in range(1, 60):
for file in os.listdir(img_root):
    # img = cv2.imread(img_root+str(i)+".png")
    img = cv2.imread(img_root+file)
    videowriter.write(img)
videowriter.release()
