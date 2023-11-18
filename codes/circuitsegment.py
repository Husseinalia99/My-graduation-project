
#circuitsegment.py
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('circuitE.jpg',0)
img1=cv2.blur(img,(15,150))
retval1, threshold1 = cv2.threshold(img1, 153, 255, cv2.THRESH_BINARY)
retval2, threshold2 = cv2.threshold(img1, 158, 255, cv2.THRESH_BINARY)

plt.figure(1)
plt.subplot(221),plt.imshow(img,cmap='gray')
plt.subplot(222),plt.imshow(img1,cmap='gray')
plt.subplot(223),plt.imshow(threshold1,cmap='gray')
plt.subplot(224),plt.imshow(threshold2,cmap='gray')
plt.show()



