# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:24:58 2022

@author: 10960
"""

import cv2
import numpy as np
import math
 
 
def psnr(img1, img2):
   mse = np.mean( (img1/255. - img2/255.) ** 2 )
   if mse < 1.0e-10:
      return 100
   PIXEL_MAX = 1
   return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

# if __name__ =='__main__':
    
#     im1 = cv2.imread('pic/b.png')
#     im2 = cv2.imread('out/water_lena1.png')
#     x = psnr(im1, im2)
#     print("psnr3:",x)


# im3 = cv2.imread('out/test2.png')
# print('psnr2:',psnr(im1,im3))
