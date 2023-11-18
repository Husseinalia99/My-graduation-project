#ex1.py
import cv2


pic = cv2.imread('aa.jpg',-1)
pic1 = cv2.imread('aa.jpg',0)
pic2 = cv2.imread('aa.jpg',1)

cv2.imshow('image',pic)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('image1',pic1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('image2',pic2)
cv2.waitKey()
cv2.destroyAllWindows()

print('dimensions of pic :',pic.shape,'\ndimensions of pic1 :',pic1.shape,'\ndimensions of pic2 :',pic2.shape)
print('type of values pic :',pic.dtype,'\ntype of  values pic1 :',pic1.dtype,'\ntype of values pic2 :',pic2.dtype)

cv2.imwrite('aanew.png',pic1)


