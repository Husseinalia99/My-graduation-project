#sobel_edges.py
import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('letters.jpg',0)

h1=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
h2=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
h3=np.array([[2,1,0],[1,0,-1],[0,-1,-2]])
h4=np.array([[0,1,2],[-1,0,1],[-2,-1,0]])
h5=np.array([[1,0],[0,-1]])
h6=np.array([[0,1],[-1,0]])
img1=cv2.filter2D(img,-1,h1)
img2=cv2.filter2D(img,-1,h2)
img3=cv2.filter2D(img,-1,h3)
img4=cv2.filter2D(img,-1,h4)
img5=cv2.filter2D(img,-1,h5)
img6=cv2.filter2D(img,-1,h6)

img7=cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
img8=cv2.Sobel(img,cv2.CV_8U,1,0,ksize=7)
img9=np.absolute(cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3))
img10=np.absolute(cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3))

cv2.imshow('img',img)
cv2.waitKey(2000)
plt.figure(2)
plt.subplot(221),plt.imshow(img1,cmap='gray')
plt.subplot(222),plt.imshow(img2,cmap='gray')
plt.subplot(223),plt.imshow(img3,cmap='gray')
plt.subplot(224),plt.imshow(img4,cmap='gray')
plt.figure(3)
plt.subplot(121),plt.imshow(img5,cmap='gray')
plt.subplot(122),plt.imshow(img6,cmap='gray')
plt.figure(4)
plt.subplot(221),plt.imshow(img7,cmap='gray')
plt.subplot(222),plt.imshow(img8,cmap='gray')
plt.subplot(223),plt.imshow(img9,cmap='gray')
plt.subplot(224),plt.imshow(img10,cmap='gray')
plt.show()
