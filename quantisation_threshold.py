import numpy as num
import cv2
from matplotlib import pyplot as plt
def thresholding(pic,levels):
    a=pic.shape[0]
    b=pic.shape[1]
    factor=256//levels
    change=num.zeros((a,b)).astype('uint8')
    for i in range(0,a):
        for j in range(0,b):
            change[i,j]=(pic[i][j]//factor)*factor
    return change
def show(objects):
    image_rgb=cv2.cvtColor(objects[0],cv2.COLOR_BGR2RGB)
    plt.subplot(3,2,1)
    plt.title("Original image \n with 256 levels")
    plt.imshow(image_rgb)
    image_rgb=cv2.cvtColor(objects[1],cv2.COLOR_BGR2RGB)
    plt.subplot(3,2,2)
    plt.title("128 levels")
    plt.imshow(image_rgb)
    image_rgb=cv2.cvtColor(objects[2],cv2.COLOR_BGR2RGB)
    plt.subplot(3,2,3)
    plt.title("32 levels")
    plt.imshow(image_rgb)
    image_rgb=cv2.cvtColor(objects[3],cv2.COLOR_BGR2RGB)
    plt.subplot(3,2,4)
    plt.title("8 levels")
    plt.imshow(image_rgb)
    image_rgb=cv2.cvtColor(objects[4],cv2.COLOR_BGR2RGB)
    plt.subplot(3,2,5)
    plt.title("2 levels")
    plt.imshow(image_rgb)
    plt.show()

image1=cv2.imread("lena.pgm",cv2.IMREAD_UNCHANGED)
lena_128,lena_32,lena_8,lena_2=thresholding(image1,128),thresholding(image1,32),thresholding(image1,8),thresholding(image1,2)
items_lena=[image1,lena_128,lena_32,lena_8,lena_2]
show(items_lena)
image2=cv2.imread("peppers.pgm",cv2.IMREAD_UNCHANGED)
peppers_128,peppers_32,peppers_8,peppers_2=thresholding(image2,128),thresholding(image2,32),thresholding(image2,8),thresholding(image2,2)
items_peppers=[image2,peppers_128,peppers_32,peppers_8,peppers_2]
show(items_peppers)
