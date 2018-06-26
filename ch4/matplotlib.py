# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:57:31 2018

@author: john 

"""
import cv2
import matplotlib.pyplot as plt
import os
import numpy as np

path='ilikelzl.jpg'


    
img = cv2.imread('lzl.jpg', 0)
# 彩色图像使用 OpenCV 加载时是 BGR 模式。但是 Matplotlib 是 RGB 模式。所以彩色图像如果已经被OpenCV 读取，  它将不会被 Matplotlib 正 确显示
plt.imshow(img, cmap='gray', interpolation='bicubic')

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


