# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:30:09 2022

@author: 10960
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('out/test3.png')
def saltnoise(img):
    for k in range(1000):
        i = int(np.random.random()*img.shape[1])
        j = int(np.random.random()*img.shape[0])
        if img.ndim == 2:
            img[j,i] = 255
        elif img.ndim ==3:
            img[j,i,0] = 255
            img[j,i,1] = 255
            img[j,i,2] = 255
    return img
    # cv2.imshow('at_img',img)
    # cv2.waitKey()
    # path = input('请输入图片的保存地址：')
    # cv2.imwrite(path,img)

#cv2.imwrite('out/noise2.png',saltnoise(img))

def bright(img):
    w,h = img.shape[:2]
    for i in range(0,w):
        for j in range(0,h):
            img[i,j,0] = int(img[i,j,0]*1.1)
            img[i,j,1] = int(img[i,j,1]*1.1)
            img[i,j,2] = int(img[i,j,2]*1.1)
    return img


#cv2.imwrite('out/bright3.png',bright(img))

def dark(img):
    w,h = img.shape[:2]
    for i in range(0,w):
        for j in range(0,h):
            img[i,j,0] = int(img[i,j,0]*0.9)
            img[i,j,1] = int(img[i,j,1]*0.9)
            img[i,j,2] = int(img[i,j,2]*0.9)
    return img

# # 随意画线
def line(img):
    cv2.rectangle(img, (384,0), (510,128), (0,255,0),3)
    cv2.rectangle(img, (0,0), (300,128), (255,0,0),3)
    cv2.line(img,(0,0),(511,511),(255,0,0),5)
    cv2.line(img,(0,511),(511,0),(255,0,255),5)
    return img
    


#cv2.imwrite('out/line1.png',line(img))

# # 剪切
def chop(img):
    w,h = img.shape[:2]
    img[w-int(w*0.05):,:] = img[:int(w*0.05)]
    return img


# # 遮挡
def cover(img):
    cv2.circle(img,(256,256),63,(0,0,255),-1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'hello', (10,500), font, 4, (255,255,0),2)
    return img
    


# # 拉伸
def large(img):
    w,h = img.shape[:2]
    cv2.resize(img,(int(h*1.5),w))
    return img

# 缩小
def small(img):
    w,h = img.shape[:2]
    cv2.resize(img,(int(h*0.5),w))
    return img




