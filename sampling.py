import cv2
import numpy as num
from matplotlib import pyplot as plt
def down_sampling(pic,factor):
    a=pic.shape[0]//factor
    b=pic.shape[1]//factor
    change=num.zeros((a,b,3)).astype('uint8')
    for i in range(0,a):
        for j in range(0,b):
            for k in range(0,3):
                change[i,j,k]=pic[i*factor][j*factor][k]
    return change
def up_sampling(pic,reduced_image):
    factor=pic.shape[0]//reduced_image.shape[0]
    change=num.zeros((pic.shape[0],pic.shape[1],3)).astype('uint8')
    for i in range(0,pic.shape[0]):
        for j in range(0,pic.shape[1]):
            for k in range(0,3):
                change[i,j,k]=reduced_image[i//factor][j//factor][k]
    return change
def show(objects):
    image_rgb=cv2.cvtColor(objects[0],cv2.COLOR_BGR2RGB)
    a=objects[0].shape[0]
    b=objects[0].shape[1]
    plt.subplot(2,2,1)
    plt.title("Original image   "+ str(a)+"*"+str(b))
    plt.imshow(image_rgb)
    image_rgb=cv2.cvtColor(objects[1],cv2.COLOR_BGR2RGB)
    a=objects[1].shape[0]
    b=objects[1].shape[1]
    plt.subplot(2,2,2)
    plt.title("k=2   "+str(a)+"*"+str(b))
    plt.imshow(image_rgb)
    image_rgb=cv2.cvtColor(objects[2],cv2.COLOR_BGR2RGB)
    a=objects[2].shape[0]
    b=objects[2].shape[1]
    plt.subplot(2,2,3)
    plt.title("k=4   "+ str(a)+"*"+str(b))
    plt.imshow(image_rgb)
    image_rgb=cv2.cvtColor(objects[3],cv2.COLOR_BGR2RGB)
    a=objects[3].shape[0]
    b=objects[3].shape[1]
    plt.subplot(2,2,4)
    plt.title("k=8   "+ str(a)+"*"+str(b))
    plt.imshow(image_rgb)
    plt.show()
image1=cv2.imread("lena.jpg")
lena_down_2,lena_down_4,lena_down_8=down_sampling(image1,2),down_sampling(image1,4),down_sampling(image1,8)
lena_up_2,lena_up_4,lena_up_8=up_sampling(image1,lena_down_2),up_sampling(image1,lena_down_4),up_sampling(image1,lena_down_8)
items_lena_down=[image1,lena_down_2,lena_down_4,lena_down_8]
items_lena_up=[image1,lena_up_2,lena_up_4,lena_up_8]
show(items_lena_down)
show(items_lena_up)
image2=cv2.imread("peppers.png")
peppers_down_2,peppers_down_4,peppers_down_8=down_sampling(image2,2),down_sampling(image2,4),down_sampling(image2,8)
peppers_up_2,peppers_up_4,peppers_up_8=up_sampling(image2,peppers_down_2),up_sampling(image2,peppers_down_4),up_sampling(image2,peppers_down_8)
items_peppers_down=[image2,peppers_down_2,peppers_down_4,peppers_down_8]
items_peppers_up=[image2,peppers_up_2,peppers_up_4,peppers_up_8]
show(items_peppers_down)
show(items_peppers_up)

