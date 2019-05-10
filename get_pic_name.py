# -*- coding:utf-8 -*-
import sys

# sys.path.append('E:\\Anaconda\\libs')
import os  # os：操作系统相关的信息模块
import random  # 导入随机函数


def get_name():
    # 存放原始图片地址
    data_base_dir = "E:/workspace/mystoreroom/segnet1/test_pic"
    file_list = []  # 建立列表，用于保存图片信息
    # 读取图片文件，并将图片地址、图片名和标签写到txt文件中
    write_file_name = 'E:/workspace/mystoreroom/segnet1/SegNet/CamVid/t1.txt'
    write_file = open(write_file_name, "w")  # 以只写方式打开write_file_name文件
    for file in os.listdir(data_base_dir):  # file为current_dir当前目录下图片名
        if file.endswith(".png"):  # 如果file以png结尾
            write_name = '/test_pic/' + file  # 图片路径 + 图片名
            file_list.append(write_name)  # 将write_name添加到file_list列表最后
    sorted(file_list)  # 将列表中所有元素随机排列
    number_of_lines = len(file_list)  # 列表中元素个数
    # 将图片信息写入txt文件中，逐行写入
    for current_line in range(number_of_lines):
        write_file.write(file_list[current_line] + '\n')
    # 关闭文件
    write_file.close()



'''import numpy as np
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
'''
