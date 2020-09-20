# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 20:35:46 2020

@ Name: Abhishek Dhital
  ID  : 1001548204
"""


import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
from scipy import ndimage

def lowpassfilter(image):
    tenpoint=[.1]*10
    size=image[1].size+(10-1)  
    filtered=np.empty((np.size(image,0),size))
    n=0
    for x in image:
        temp=np.convolve(x,tenpoint)
        filtered[n]=temp
        n+=1
    return filtered
    
def showImg(caption,image):    #function to show the passed image file with the caption parameter as the title
    plt.imshow(image,cmap="gray")
    plt.title(caption)
    plt.axis("off")
    plt.show()

def edgeDetection(image):
    h=[1,-1]
    size=image[1].size+(2-1)
    filtered=np.empty((size,size))
    n=0
    for x in image:
        temp=np.convolve(x,h)
        filtered[n]=temp
        n+=1
    return filtered
    
    
        
img1=img.imread('boat.512.tiff')
showImg("original boat image",img1)
showImg("blurred boat image",lowpassfilter(img1))
showImg("edge detected boat image",edgeDetection(img1))

img2=img.imread('clock-5.1.12.tiff')
showImg("original clock image",img2)
showImg("blurred clock image",lowpassfilter(img2))
showImg("edge detected clock image",edgeDetection(img2))


img3=img.imread('man-5.3.01.tiff')
showImg("original man image",img3)
showImg("blurred man image",lowpassfilter(img3))
showImg("edge detected man image",edgeDetection(img3))

img4=img.imread('tank-7.1.07.tiff')
showImg("original tank image",img4)
showImg("blurred tank image", lowpassfilter(img4))
showImg("edge detected tank image", edgeDetection(img4))

img4=img.imread('darinGrayNoise.jpg')
showImg("original image with salt and pepper noise",img4)
showImg("image after low pass filter",lowpassfilter(img4))
showImg("image after median filter",ndimage.median_filter(img4,5))
showImg("edge detected darin", edgeDetection(img4))
showImg("edge detected darin II", edgeDetection(ndimage.median_filter(img4,5)))





    
  
    



    



        




