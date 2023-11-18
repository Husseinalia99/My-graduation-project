#noiseadd1.py
import skimage
import matplotlib.pyplot as plt
import cv2
img=cv2.imread('coins.png',0)
img1=skimage.util.random_noise(img,"gaussian",mean=0,var=0.01)
img11=skimage.util.random_noise(img,"gaussian",mean=0,var=0.05)
img2=skimage.util.random_noise(img,'s&p',amount=0.01)
img22=skimage.util.random_noise(img,'s&p',amount=0.05)
img3=skimage.util.random_noise(img,'speckle',mean=0,var=0.01)
img33=skimage.util.random_noise(img,'speckle',mean=0,var=0.05)
plt.figure(1)
plt.subplot(321),plt.imshow(img1,cmap='gray')
plt.subplot(322),plt.imshow(img11,cmap='gray')
plt.subplot(323),plt.imshow(img2,cmap='gray')
plt.subplot(324),plt.imshow(img22,cmap='gray')
plt.subplot(325),plt.imshow(img3,cmap='gray')
plt.subplot(326),plt.imshow(img33,cmap='gray')
plt.show()
