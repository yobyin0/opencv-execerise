# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:43:02 2018

@author: john
"""
import cv2

'''flag=-1时，8位深度，原通道
flag=0，8位深度，1通道
flag=1,   8位深度  ，3通道
flag=2，原深度，1通道
flag=3,  原深度，3通道
flag=4，8位深度 ，3通道
'''

img=cv2.imread('..//pic//lzl.jpg',3) # 
cv2.imshow('lzl',img)

k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('..pic//lzl.png', img)
    cv2.destroyAllWindows()

