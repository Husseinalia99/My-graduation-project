#laplacian_edges.py
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('letters.jpg',0)

h1=np.array([[1,1,1],[1,-8,1],[1,1,1]])
img1=cv2.filter2D(img,-1,h1)
img2=np.absolute(cv2.Laplacian(img,cv2.CV_64F))
plt.figure(1)
plt.subplot(131),plt.imshow(img,cmap='gray')
plt.subplot(132),plt.imshow(img1,cmap='gray')
plt.subplot(133),plt.imshow(img2,cmap='gray')
plt.show()



