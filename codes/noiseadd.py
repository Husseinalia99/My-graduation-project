import cv2
import numpy as np
img=cv2.imread('coins.png',0)
img=img/255.0
g=np.random.normal(0,0.04,img.shape)
noise=np.zeros(img.shape,np.float32)
noise=img+g
cv2.normalize(noise,noise,0,255,cv2.NORM_MINMAX,dtype=-1)
noise=noise.astype(np.uint8)
cv2.imshow('orginal',img)
cv2.waitKey(2000)
cv2.imshow('image after additional noise ',noise)
cv2.waitKey(0)
cv2.imwrite('coins1.png',noise)
i=cv2.imread('coins1.png',0)
cv2.imshow('additional noise',i)
cv2.waitKey(0)

