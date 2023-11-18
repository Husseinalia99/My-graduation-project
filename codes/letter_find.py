#letter_find.py
import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('text.png',0)/255.0
bw=img[32:45,88:98]
center=(6,6)
m=cv2.getRotationMatrix2D(center,-180,1.0)
m1=cv2.getRotationMatrix2D(center,-90,1.0)
rotated=cv2.warpAffine(bw,m,(256,256))
rotated1=cv2.warpAffine(bw,m1,(256,256))
c=np.abs(np.fft.ifft2(np.multiply(np.fft.fft2(img),np.fft.fft2(rotated))))
c1=np.abs(np.fft.ifft2(np.multiply(np.fft.fft2(img),np.fft.fft2(rotated1))))
retval, im = cv2.threshold(c, 60, 255, cv2.THRESH_BINARY)
retval, im1 = cv2.threshold(c1, 60, 255, cv2.THRESH_BINARY)

cv2.imshow('im',im)
cv2.waitKey(2000)
cv2.imshow('im1',im1)
cv2.waitKey(0)

