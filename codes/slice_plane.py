#slice_plane.py
import cv2
import numpy as np
from matplotlib import pylab as plt
img=cv2.imread('iris.png',0)
cv2.imshow('eye',img)
cv2.waitKey(2000)
plt.figure(1)
for i in range (8):
    b = np.ones(img.shape[:], np.uint8)*pow(2,i)
    c=cv2.bitwise_and(b,img)
    plt.subplot(2,4,i+1),plt.imshow(c, cmap ='gray', interpolation ='bicubic'),plt.title('bit %i' %i)
plt.show()



