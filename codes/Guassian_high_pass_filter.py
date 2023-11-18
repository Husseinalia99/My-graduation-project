#Guassian_high_pass_filter.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cameraman.jpg', 0)/255.0
f =np.fft.fftshift( np.fft.fft2(img))
rows, cols = img.shape
y,x = np.ogrid[-rows//2:rows//2, -cols//2:cols//2]
z = np.sqrt((x) ** 2 + (y) ** 2 )
D0 = 60
h=1-np.exp((-1*z*z)/(2*D0*D0))
n = f * h
img_back = np.abs(np.fft.ifft2(np.fft.ifftshift(n)))

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.subplot(2, 2, 2), plt.imshow(h, cmap='gray')
plt.subplot(2, 2, 3), plt.imshow(np.log(1+np.abs(n)), cmap='gray')
plt.subplot(2, 2, 4), plt.imshow(img_back, cmap='gray')
plt.show()


