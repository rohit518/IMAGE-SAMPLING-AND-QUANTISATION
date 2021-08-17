import numpy as num
import cv2
from matplotlib import pyplot as plt
def k_means(pic,levels):
    q=pic.reshape((-1,3))
    q=num.float32(q)
    act=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,0.1)
    ret,label,center=cv2.kmeans(q,levels,None,act,10,cv2.KMEANS_RANDOM_CENTERS)
    center=num.uint8(center)
    change=center[label.flatten()]
    change=change.reshape((pic.shape))
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
    
image1=cv2.imread("lena.pgm")
lena_128,lena_32,lena_8,lena_2=k_means(image1,128),k_means(image1,32),k_means(image1,8),k_means(image1,2)
items_lena=[image1,lena_128,lena_32,lena_8,lena_2]
show(items_lena)
image2=cv2.imread("peppers.pgm")
peppers_128,peppers_32,peppers_8,peppers_2=k_means(image2,128),k_means(image2,32),k_means(image2,8),k_means(image2,2)
items_peppers=[image2,peppers_128,peppers_32,peppers_8,peppers_2]
show(items_peppers)
