#forth.py
import cv2
import matplotlib.pyplot as plt
from skimage.morphology import dilation,erosion,rectangle,opening,closing,square,disk
import numpy as  np
a=rectangle(1,3,np.uint8)
#a=np.array([[1,1,1]])
b=np.array([[0,1,0,1,1,1,0,0],[0,1,0,1,1,0,0,0],[0,1,1,1,1,0,0,0]])
c=dilation(b,a)
d=erosion(b,a)
print(b)
print(c)
print(d)
#######################################################
img=cv2.imread('shapes.jpg',0)
bin=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)
se=square(7,np.uint8)
dil=dilation(bin,se)
ero=erosion(bin,se)
op=opening(bin,se)
cl=closing(bin,se)
I=cv2.subtract(dil,img)
plt.subplot(231),plt.imshow(img,cmap='gray'),plt.title('orginal')
plt.subplot(232),plt.imshow(dil,cmap='gray'),plt.title('dilation')
plt.subplot(233),plt.imshow(ero,cmap='gray'),plt.title('erosion')
plt.subplot(234),plt.imshow(op,cmap='gray'),plt.title('opening')
plt.subplot(235),plt.imshow(dil,cmap='gray'),plt.title('closing')
plt.subplot(236),plt.imshow(I,cmap='gray'),plt.title('external piremeters')
plt.show()
