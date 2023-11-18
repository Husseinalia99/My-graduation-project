#adjust.py
import cv2
import numpy as np

import matplotlib.pyplot as plt
from skimage import exposure
img=cv2.imread('rice1.jpg')
print(np.max(img))
print(np.min(img))

img1=exposure.rescale_intensity(img,out_range=(77,175))
img2=exposure.rescale_intensity(img,out_range=(0,255))
plt.figure(1)
plt.subplot(231),plt.imshow(img,cmap='gray')
plt.subplot(232),plt.imshow(img1,cmap='gray')
plt.subplot(233),plt.imshow(img2,cmap='gray')
plt.subplot(234),plt.hist(img.ravel(),256,[0,256])
plt.subplot(235),plt.hist(img1.ravel(),256,[0,256])
plt.subplot(236),plt.hist(img2.ravel(),256,[0,256])
plt.xlim([0,255])
plt.show()
