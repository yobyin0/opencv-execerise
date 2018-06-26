# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:16:18 2018

@author: john
"""

import cv2

img = cv2.imread('..//pic//lzl.jpg', 0)  # gray
print(img.shape)

img = cv2.imread('..//pic//lzl.jpg')
# print(img.shape)
rows, cols, ch = img.shape
print('height:', rows, 'width:', cols, 'channel:', ch)

print(img.size)
print(img.dtype)#uint8