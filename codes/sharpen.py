#sharpen.py
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import unsharp_mask
img=cv2.imread('brain.jpg',0)
enhanced_im=unsharp_mask(img,radius=5,amount=2)
enhanced_im1=unsharp_mask(img,radius=20,amount=2)
h1=np.array([[1, 0 ,-1],[2 ,1 ,-2],[1 ,0 ,-1]])
img1=cv2.filter2D(img,-1,h1)
h2=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
img2=cv2.filter2D(img,-1,h2)
img3=cv2.imread('old_house.png',0)
img4=cv2.filter2D(img3,-1,h1)
img5=cv2.filter2D(img3,-1,h2)
plt.figure(1)
plt.subplot(131),plt.imshow(img,cmap='gray')
plt.subplot(132),plt.imshow(img1,cmap='gray')
plt.subplot(133),plt.imshow(img2,cmap='gray')
plt.figure(2)
plt.subplot(131),plt.imshow(img,cmap='gray')
plt.subplot(132),plt.imshow(enhanced_im,cmap='gray')
plt.subplot(133),plt.imshow(enhanced_im1,cmap='gray')
plt.figure(3)
plt.subplot(131),plt.imshow(img3,cmap='gray')
plt.subplot(132),plt.imshow(img4,cmap='gray')
plt.subplot(133),plt.imshow(img5,cmap='gray')
plt.show()


