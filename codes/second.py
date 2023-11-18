#second.py
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('noisy.jpg',-1)
cv2.imshow('noisy image',img)
cv2.waitKey(200)
img=cv2.medianBlur(img,9)
cv2.imshow('blured image',img)
cv2.waitKey(200)
h1=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
img=cv2.filter2D(img,-1,h1)
cv2.imshow('enhanced image',img)
cv2.waitKey(200)
color=('r','b','g')
plt.figure(5)
for i,col in enumerate(color):
    histeq = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histeq,color=col)
    plt.xlim([0,256])
plt.show()