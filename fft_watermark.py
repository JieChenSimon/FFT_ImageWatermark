# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:25:08 2022

@author: 10960
"""


import numpy as np
import cv2
import math


#import pywt  # 离散小波变换
import random



ALPHA = 2  # 混杂强度
# 读取原始图像和水印图像
# numpy的傅氏变换
#im = cv2.imread('1.jpg')/255  # 原始图像
#mark = cv2.imread('lutos.jpg')/255  # 原始图像
# im = cv2.imread('pic/biff.png')/255  # 原始图像
# mark = cv2.imread('pic/mark3.png')/255  # 原始图像
def fft_e(im_path,mark_path):
    ALPHA = 2  # 混杂强度
    im = cv2.imread(im_path)/255
    mark = cv2.imread(mark_path)/255
     # 显示原始图像
    cv2.imshow("ori", im)
    cv2.waitKey()
     # 显示水印图像
    cv2.imshow("mark", mark)
    cv2.waitKey()
    imsize = im.size
    im_height, im_width, im_channel = np.shape(im)
    #im_height, im_width = np.shape(im)
    mark_height, mark_width = mark.shape[0], mark.shape[1]
    # 原图像傅里叶变换
    im_f = np.fft.fft2(im)  # 快速傅氏变换
    im_f = np.fft.fftshift(im_f)  # 频移
    
    # 随机编码
    x = list(range(math.floor(im_height/2)))
    y = list(range(im_width))
    # random.seed(im_height+im_width)
    # random.shuffle(x)
    # random.shuffle(y)
    temp = np.zeros(im.shape)
    path = input('请输入含水印图像的保存地址：')
    for i in range(math.floor(im_height/2)):
        for j in range(im_width):
            if x[i] < mark_height and y[j] < mark_width:
                temp[i][j] = mark[x[i]][y[j]]
                temp[im_height-i-1][im_width-j-1] = temp[i][j]
                # 以上进行对称
     
        # random
        x, y = list(range(math.floor(im_height/2))), list(range(im_width))
         # random.seed(im_height+im_width)
         # random.shuffle(x)
         # random.shuffle(y)
        tmp = np.zeros(im.shape)  # 与源图像等大小的模板，用于加上水印
        for i in range(math.floor(im_height / 2)):
            for j in range(im_width):
                if x[i] < mark_height and y[j] < mark_width:
                     # 对称
                     tmp[i][j] = mark[x[i]][y[j]]
                     tmp[im_height-i-1][im_width-j-1] = tmp[i][j]
       
         # 混杂
        res_f = im_f + ALPHA * tmp
        # plt.imshow(np.log(np.abs(res_f)))p
         # 逆变换
        res = np.fft.ifftshift(res_f)
        res = np.abs(np.fft.ifft2(res)) *255  # 回乘255
          # 显示加密后的图像
        # cv2.imshow("嵌入水印图像", res)
        # cv2.waitKey()
         # 保存
         #cv2.imwrite('test11', res, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        #path = input('请输入含水印图像的保存地址：')
        cv2.imwrite(path,res)
    # cv2.imshow("嵌入水印图像", res)
    # cv2.waitKey()
    # return res
    #      #cv2.imshow('im_ad_w',res)
    
# if __name__=='__main__':
#     im_path = input("请输入载体图像的路径")
#     mark_path = input('请输入水印图像的路径')
#     fft_e(im_path, mark_path)
   # cv2.imshow("嵌入水印的图像",img)
    
