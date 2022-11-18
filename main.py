# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:46:49 2022

@author: 10960
"""

from fft_watermark import *
from ifft_watermark import *
from psnr import *
from att import *
import cv2 as cv




def showimg(img):
     cv.imshow('at_img',img)
     cv.waitKey()
     path = input('请输入图片的保存地址：')
     cv.imwrite(path,img)
def test1():
    print('---------------说明--------------')
    print("1:傅里叶变换嵌入水印     2：提取水印      3：对水印图像进行攻击  psnr:图像psnr分析   end:退出   go:继续执行")
    #print("请选择功能模块")
    #code = input()
    while(input('请选择继续(go)还是退出(end)')!='end'):
        code = input('请选择功能模块')
        if code =="1":
            print("请输入载体图像路径")
            im_path = input()
            print("请输入水印图像路径")
            mark_path = input()
            fft_e(im_path, mark_path)
            print("水印嵌入完成，已保存在指定路径下！")
        elif code== '2':
           print("请输入载体图像路径")
           im_path = input()
           print("请输入嵌入水印图像的路径")
           im_mark_path = input()
           ifft_d(im_path, im_mark_path)
           print('水印提取完成，已保存在指定路径下！')
        elif code=='3':
            print("请输入要进行攻击的图片路径")
            at_path = input()
            img = cv.imread(at_path)
            print("------------------请选择要攻击的方式------------------")
            print("saltnoise:椒盐噪声    bright：增加亮度       dark:降低亮度    line:随意画线")
            print("cover:遮挡           chop:剪切             large:拉伸       small:缩小")
            mode = input()
            if mode =='saltnoise':
                at_img = saltnoise(img)
                showimg(at_img)
                print('保存完成！')
            elif mode =='bright':
                at_img = bright(img)
                showimg(at_img)
                print('保存完成！')
            elif mode =='dark':
                at_img = dark(img)
                showimg(at_img)
                print('保存完成！')
            elif mode =='line':
                at_img = line(img)
                showimg(at_img)
                print('保存完成！')
            elif mode =='cover':
                at_img = cover(img)
                showimg(at_img)
                print('保存完成！')
            elif mode =='chop':
                at_img = chop(img)
                showimg(at_img)
                print('保存完成！')
            elif mode =='large':
                at_img = large(img)
                showimg(at_img)
                print('保存完成！')
            elif mode =='small':
                at_img = small(img)
                showimg(at_img)
                print('保存完成！')
            else:
                print('输入错误！')
       
        if code =='psnr':
            img1_path = input('请输入载体图像的路径')
            img2_path = input('请输入嵌入水印后图像的路径')
            img1 = cv.imread(img1_path)
            img2 = cv.imread(img2_path)
            psnr_value = psnr(img1, img2)
            print('psnr:',psnr_value)
            

if __name__=="__main__":
    test1()
