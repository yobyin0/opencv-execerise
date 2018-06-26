# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:12:25 2018

@author: john
"""
'''
 如果报错请先检查摄像头
'''


import cv2
import numpy 
# 一般笔记本内置摄像头的参数是0
cap.release() ##先realse 一下有时不释放呀
cap=cv2.VideoCapture(0)


frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)#4 ，720
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)#3   ，1280
frame_height=int(480/frame_width*frame_height)#270
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)#高
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
while cap.isOpened():  
    # 检查是否成功初始化，否则就 使用函数 cap.open()
    # Capture frame-by-frame
    ret, frame = cap.read()  # ret 返回一个布尔值 True/False
    # print('frame shape:',frame.shape)#(720, 1280, 3)

    frame = cv2.flip(frame, flipCode=1)  # 左右翻转,使用笔记本电脑摄像头才有用。
    # flipCode：翻转方向：1：水平翻转；0：垂直翻转；-1：水平垂直翻转

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    cv2.setWindowTitle('frame', 'COLOR_BGR2GRAY')

    # Property=cv2.getWindowProperty('frame',0)#无用

    # if cv2.waitKey(1) & 0xFF == ord('q'):#不行
    #     break
    key = cv2.waitKey(delay=10)
    if key == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()