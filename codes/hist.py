#hist.py
import cv2
import matplotlib.pyplot as plt
import numpy as np

im=cv2.imread('pout.tif',0)
im1=cv2.add(im,40)
im2=cv2.subtract(im,70)
im3=cv2.multiply(im,2)
im4=cv2.divide(im,4)

plt.figure(1)
plt.subplot(5,2,1),plt.imshow(im,cmap='gray')
plt.subplot(5,2,2),plt.hist(im.ravel(),256,[0,256])
plt.subplot(5,2,3),plt.imshow(im1,cmap='gray')
plt.subplot(5,2,4),plt.hist(im1.ravel(),256,[0,256])
plt.subplot(5,2,5),plt.imshow(im2,cmap='gray')
plt.subplot(5,2,6),plt.hist(im2.ravel(),256,[0,256])
plt.subplot(5,2,7),plt.imshow(im3,cmap='gray')
plt.subplot(5,2,8),plt.hist(im3.ravel(),256,[0,256])
plt.subplot(5,2,9),plt.imshow(im2,cmap='gray')
plt.subplot(5,2,10),plt.hist(im4.ravel(),256,[0,256])
plt.xlim([0,255])

plt.figure(2)
equ = cv2.equalizeHist(im)
histeq,bins = np.histogram(equ.ravel(),256,[0,256])

plt.subplot(121),plt.imshow(equ,cmap='gray')
plt.subplot(122),plt.plot(histeq)
plt.xlim([0,255])

plt.figure(3)
mask = np.zeros(im.shape[:2], np.uint8)
mask[20:120, 50:170] = 255
imm=im[20:120, 50:170]

histt = cv2.calcHist([im],[0],mask,[256],[0,256])
hist=cv2.calcHist([im],[0],None,[256],[0,256])

plt.subplot(2,2,1),plt.imshow(im,cmap='gray')
plt.subplot(2,2,2),plt.plot(hist)
plt.subplot(2,2,3),plt.imshow(imm,cmap='gray')
plt.subplot(2,2,4),plt.plot(histt)
plt.xlim([0,255])



plt.show()









