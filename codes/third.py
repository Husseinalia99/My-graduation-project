#third.py
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import label2rgb
from skimage.morphology import opening,square,label
a=np.array([[1,0,1,0,1,1],[1,1,0,1,1,0],[1,0,0,0,0,1],[0,0,1,0,1,1],[0,1,1,0,0,0]])
label_img1=label(a,connectivity=1)
label_img2=label(a,connectivity=2)
print(a,'\n\n')
print(label_img1,'\n\n')
print(label_img2)
########################################################
img=cv2.imread('rice.png',-1)
cv2.imshow('rice',img)
cv2.waitKey(200)
bin=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)
cv2.imshow('binary rice',bin)
cv2.waitKey(200)
binc=opening(bin,square(3))
cv2.imshow('openning binary rice',binc)
cv2.waitKey(200)
label_img=label(binc,connectivity=1)
#label_img=label(binc,connectivity=2)
color_label_img=label2rgb(label_img,colors=[[255,255,0],[255,0,255],[0,0,0],[0,255,0],[0,0,255],[90,70,60],[10,10,0],[90,89,67],[5,6,8],[23,56,45]])
#color_label_img=label2rgb(label_img)
plt.subplot(131),plt.imshow(color_label_img)
plt.subplot(132),plt.imshow(label_img,cmap='jet')
plt.subplot(133),plt.imshow(label_img,cmap='spring')
plt.show()

