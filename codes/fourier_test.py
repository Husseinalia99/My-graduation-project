#fourier_test.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('zee.jpg',0)/255.0
f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)
magnitude_spectrum=np.log(1+np.abs(fshift))

dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
magnitude_spectrum1 = np.log(1+cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.figure(1)
plt.subplot(131),plt.imshow(magnitude_spectrum,cmap='gray')
plt.subplot(132),plt.imshow(img,cmap='gray')
plt.subplot(133),plt.imshow(magnitude_spectrum1,cmap='gray')

img=cv2.imread('vee.jpg',0)/255.0
dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
magnitude_spectrum1 = np.log(1+cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.figure(2)
plt.subplot(321),plt.imshow(img,cmap='gray')
plt.subplot(322),plt.imshow(magnitude_spectrum1,cmap='gray')

img=cv2.imread('k.jpg',0)/255.0
dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
magnitude_spectrum1= np.log(1+cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.figure(2)
plt.subplot(323),plt.imshow(img,cmap='gray')
plt.subplot(324),plt.imshow(magnitude_spectrum1,cmap='gray')
img=cv2.imread('ech.jpg',0)/255.0
dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
magnitude_spectrum1=  np.log(1+cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.figure(2)
plt.subplot(325),plt.imshow(img,cmap='gray')
plt.subplot(326),plt.imshow(magnitude_spectrum1,cmap='gray')

img=cv2.imread('square1.jpg',0)/255.0
dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
magnitude_spectrum1=  np.log(1+cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.figure(3)
plt.subplot(221),plt.imshow(img,cmap='gray')
plt.subplot(222),plt.imshow(magnitude_spectrum1,cmap='gray')
img=cv2.imread('square2.jpg',0)/255.0
dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
magnitude_spectrum1=  np.log(1+cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.subplot(223),plt.imshow(img,cmap='gray')
plt.subplot(224),plt.imshow(magnitude_spectrum1,cmap='gray')
plt.show()

