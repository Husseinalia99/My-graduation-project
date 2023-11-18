#edge_detection2.py
import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage.morphology as mp
img=cv2.imread('shapes.jpg',0)
h1=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
img1=cv2.filter2D(img,-1,h1)
#ret,img2=cv2.threshold(img1,253,255,cv2.THRESH_BINARY)
img3=mp.area_opening(img1,150)
plt.figure(1)
plt.subplot(131),plt.imshow(img1,cmap='gray')
#plt.subplot(132),plt.imshow(img2,cmap='gray')
plt.subplot(133),plt.imshow(img3,cmap='gray')
plt.show()
