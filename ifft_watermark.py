# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 13:13:09 2022

@author: 10960
"""

import cv2
import numpy as np
import random
import math


#ALPHA = 5  # 混杂强度

# ori = cv2.imread('pic/biff.png')/255
# im = cv2.imread('out/bright3.png',)/255
def ifft_d(ori_path,wim_path):
    ALPHA = 2  # 混杂强度
    ori = cv2.imread(ori_path)/255
    im = cv2.imread(wim_path)/255
    im_height, im_width, im_channel = np.shape(ori)
        # 源图像与水印图像傅里叶变换
    ori_f = np.fft.fft2(ori)
    ori_f = np.fft.fftshift(ori_f)
    im_f = np.fft.fft2(im)
    im_f = np.fft.fftshift(im_f)
    mark = np.abs((im_f - ori_f) /  ALPHA)
    #cv2.imwrite('out/1.png',mark)
    #res = np.zeros(ori.shape)
    
    # p = np.fft.ifftshift(im)
    # p = np.fft.ifft2(p)
    # p = np.abs(p)
    # mark = np.abs((ori -p ))
    # cv2.imwrite('t1.png',mark)
    res = np.zeros(mark.shape)
    
        # 获取随机种子
    x, y = list(range(math.floor(im_height/2))), list(range(im_width))
    # random.seed(im_height+im_width)
    # random.shuffle(x)
    # random.shuffle(y)
    path = input('请输入提取水印的保存地址：')
    for i in range(math.floor(im_height / 2)):
        for j in range(im_width):
                res[x[i]][y[j]] = mark[i][j]*255
                res[im_height-i-1][im_width-j-1] = res[i][j]
    #cv2.imwrite(res_path, res, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    # 显示加密后的图像
    #cv2.imshow("提取的水印图像", res)
    #cv2.waitKey()
    cv2.imwrite(path,res)
 
# if __name__=='__main__':
#     im_path = input("请输入载体图像的路径")
#     mark_path = input('请输入含水印图像的路径')
#     ifft_d(im_path, mark_path)
   