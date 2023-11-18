#ex1.py
import cv2
im=cv2.imread('coins.png',-1)
cv2.imshow('coins',im)
cv2.waitKey(3000)
h,w=im.shape[:2]
print('shape is :',im.shape,h,'  ',w)
h1=h//2  #h1=int (h/2)
w1=w//2 #w1=int(w/2)
im1=im[0:h1,0:w1]
cv2.imshow('crop coins',im1)
cv2.waitKey(3000)
center=(w1,h1)
m=cv2.getRotationMatrix2D(center,+45,1.0)
m1=cv2.getRotationMatrix2D(center,-45,0.5)
rotated=cv2.warpAffine(im,m,(w,h))
rotated1=cv2.warpAffine(im,m1,(w,h))
print('shape after rotation is :',rotated.shape)
cv2.imshow('rotation1',rotated)
cv2.waitKey(3000)
cv2.imshow('rotation2',rotated1)
cv2.waitKey(3000)
resized=cv2.resize(im,(200,100))
cv2.imshow('resized',resized)
cv2.waitKey(3000)
scale_percent=60/100
h1=int(h*scale_percent)
w1=int(w*scale_percent)

resized1=cv2.resize(im,(w1,h1))
print('shape after resized is :',resized1.shape)
cv2.imshow('resized1',resized1)
cv2.waitKey(3000)

scale_percent=220/100
h2=int(h*scale_percent)
w2=int(w*scale_percent)

resized2=cv2.resize(im,(w2,h2))
print('shape after resized is :',resized2.shape)
cv2.imshow('resized2',resized2)
cv2.waitKey(0)
