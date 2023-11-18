#first.py
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('peppers.png',-1)
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]
cv2.imshow('peppers',img)
cv2.waitKey(200)
cv2.imshow('blue',b)
cv2.waitKey(200)
cv2.imshow('green',g)
cv2.waitKey(200)
cv2.imshow('red',r)
cv2.waitKey(200)
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img1,cv2.COLOR_GRAY2RGB)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('convert colored image to gray image',img1)
cv2.waitKey(200)
plt.figure(5)
plt.subplot(131),plt.imshow(img)
plt.subplot(132),plt.imshow(img2)
plt.subplot(133),plt.imshow(img3)
plt.show()