#linearfilter1.py
import numpy as np
import matplotlib.pyplot as plt
import cv2

h1=np.ones((3,3),np.float32)/9
h2=np.ones((5,5),np.float32)/25
h3=np.array([[1,2,1],[2,4,2],[1,2,1]])/16

h4=np.array([[1 ,4,6,4, 1],[4 ,16, 24 ,16, 4],[6 ,24, 36, 24 ,6],[4 ,16, 24 ,16, 4],[1 ,4,6,4, 1]])/256
img=cv2.imread('coins1.png',0)
imgh1=cv2.filter2D(img,-1,h1)
imgh2=cv2.filter2D(img,-1,h2)
imgh3=cv2.filter2D(img,-1,h3)
imgh4=cv2.filter2D(img,-1,h4)
imgm1=cv2.blur(img,(3,3))
imgm2=cv2.blur(img,(5,5))
imgg1=cv2.GaussianBlur(img,(3,3),0)
imgg2=cv2.GaussianBlur(img,(5,5),0)
imgw=cv2.bilateralFilter(img,3,75,75)
print(imgh1[0:3,0:3])
print(imgm1[0:3,0:3])
print(imgh3[0:3,0:3])
print(imgg1[0:3,0:3])
print(img[0:3 , 0:3])
print(img.shape)
cv2.imshow('img',img)
cv2.waitKey(2000)
cv2.imshow('imgh1',imgh1)
cv2.waitKey(2000)
cv2.imshow('imgh2',imgh2)
cv2.waitKey(2000)
cv2.imshow('imgh3',imgh3)
cv2.waitKey(2000)
cv2.imshow('imgh4',imgh4)
cv2.waitKey(2000)
cv2.imshow('imgm1',imgm1)
cv2.waitKey(2000)
cv2.imshow('imgm2',imgm2)
cv2.waitKey(2000)
cv2.imshow('imgg1',imgg1)
cv2.waitKey(2000)
cv2.imshow('imgg2',imgg2)
cv2.waitKey(2000)
cv2.imshow('imgw',imgw)
cv2.waitKey(0)