#canny_edges.py
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('14.jpg',0)
img2=cv2.Canny(img,100,100)
plt.figure(1)
plt.subplot(222),plt.imshow(img2,cmap='gray')
plt.show()