#gray_slice_1.py
import cv2
import numpy as np
img=cv2.imread('car.jpg',-1)
cv2.imshow('colored car',img)
cv2.waitKey(3000)
img1=np.zeros(img.shape[:],np.uint8)
for m in range (3):
  for i in range (img.shape[0]):
    for j in range(img.shape[1]):
        
        if img[i,j,m]>250 and img[i,j,m]<255:
            img1[i,j,m]=255
cv2.imshow('colored car ,gray scale[250-255]',img1)
cv2.waitKey(0)
