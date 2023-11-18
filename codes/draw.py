#draw.py
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = np.zeros((512,1000,3), np.uint8)

cv2.line(img,(0,0),(511,511),(0,0,255),5)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.circle(img,(447,63), 63, (255,0,0), -1)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
pts = np.array([[70,215],[170,215],[220,260],[30,260]], np.int32)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(510,500), font, 4,(255,255,255),2)
cv2.polylines(img,[pts],True,(0,255,255))
plt.imshow(img)
plt.show()
