#gamma.py
import cv2
from matplotlib import pyplot as plt
import numpy as np
from skimage import exposure

img=cv2.imread('rice.png',0)

img1=exposure.adjust_gamma(img,3)
img2=exposure.adjust_gamma(img,0.1)

#img=img/255.0
#img1=cv2.pow(img,3)
#img2=cv2.pow(img,0.1)

x=np.linspace(0,1,10)

plt.figure(1)
plt.subplot(231),plt.imshow(img,cmap='gray'),plt.title('orginal image')
plt.subplot(232),plt.imshow(img1,cmap='gray'),plt.title('Reduce illumination')
plt.subplot(233),plt.imshow(img2,cmap='gray'),plt.title('add illumination')
plt.subplot(235),plt.plot(x,cv2.pow(x,3)),plt.title('gamma >1')
plt.subplot(236),plt.plot(x,cv2.pow(x,0.1)),plt.title('gamma <1')
plt.xlim([0, 1])

plt.show()