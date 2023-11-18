#edge_detection1.py
import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage.morphology as mp
img=cv2.imread('house.jpg',0)
h1=np.array([[2,1,0],[1,0,-1],[0,-1,-2]])
img1=cv2.filter2D(img,-1,h1)
print(np.max(img1))
retval, img2 = cv2.threshold(img1, 230, 255, cv2.THRESH_BINARY)

img3=mp.area_opening(img2,20)
plt.figure(1)
plt.subplot(131),plt.imshow(img1,cmap='gray')
plt.subplot(132),plt.imshow(img2,cmap='gray')
plt.subplot(133),plt.imshow(img3,cmap='gray')
plt.show()
