# import tensorflow as tf
# from tensorflow.python.framework import ops
# from tensorflow.python.framework import dtypes
# import os, sys
# import numpy as np
# import math
# import skimage
# import skimage.io
#

import os

from matplotlib import pyplot as plt

from PIL import Image

import cv2

# im = Image.open("E:\\workspace\\mystoreroom\\segnet1\\SegNet\\CamVid\\trainannot\\0001TP_006690.png")
im = "E:\\workspace\\mystoreroom\\segnet1\\SegNet\\CamVid\\testannot\\0001TP_008550.png"
img = cv2.imread(im, 0)
plt.imshow(img)
plt.savefig("E:\\workspace\\mystoreroom\\segnet1\\SegNet\\CamVid\\testimg")
plt.show()
