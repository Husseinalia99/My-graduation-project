#ex2.py
import cv2
im1=cv2.imread('text1.png',0)

im2=cv2.imread('mask.jpg',0)

im2=cv2.resize(im2,im1.shape)

imand=cv2.bitwise_and(im1,im2)
imor=cv2.bitwise_or(im1,im2)
imxor=cv2.bitwise_xor(im1,im2)
maskinv=cv2.bitwise_not(im2)
cv2.imshow('text',im1)
cv2.waitKey(3000)
cv2.imshow('mask',im2)
cv2.waitKey(3000)
cv2.imshow('and',imand)
cv2.waitKey(3000)
cv2.imshow('or',imor)
cv2.waitKey(3000)
cv2.imshow('xor',imxor)
cv2.waitKey(3000)
cv2.imshow("not",maskinv)
cv2.waitKey(3000)
cv2.destroyAllWindows()
