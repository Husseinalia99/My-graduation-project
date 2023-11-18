#ex2.py
import cv2

img=cv2.imread('aa.jpg',0)
cv2.imshow('image',img)

if cv2.waitKey(0)==27:
  cv2.imwrite('messigray.png',img)

cv2.destroyAllWindows()
