#gray_slice_2.py
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('moon.jpg',0)
img1=img.copy()

h,w=img.shape


for i in range (h):
   for j in range(w):

      if (img[i,j]>0 and img[i,j]<50):
            img1[i,j]=img1[i,j]*5


plt.figure(1)
plt.subplot(221),plt.imshow(img,cmap='gray')
plt.subplot(222),plt.imshow(img1,cmap='gray')
plt.subplot(223),plt.hist(img.ravel(),256,[0,256])
plt.subplot(224),plt.hist(img1.ravel(),256,[0,256])
plt.xlim([0,255])
plt.show()

