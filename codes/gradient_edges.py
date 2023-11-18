#gradient_edges.py
import numpy as np
import matplotlib.pyplot as plt
a=np.zeros((200,200))
b=np.zeros((200,200))
b[:,100:200]=1
k=0
for i in range(200):
    a[:,i]=k
    k=k+0.005

a[:,50]=a[:,50]+0.005
a[:,160]=a[:,160]+0.005

a1=np.gradient(a,axis=1)
a2=np.gradient(a1,axis=1)
b1=np.gradient(b,axis=1)
b2=np.gradient(b1,axis=1)
plt.figure(1)
plt.subplot(131),plt.imshow(b,cmap='gray')
plt.subplot(132),plt.imshow(b1,cmap='gray')
plt.subplot(133),plt.imshow(b2,cmap='gray')
plt.figure(2)
plt.subplot(131),plt.imshow(a,cmap='gray')
plt.subplot(132),plt.imshow(a1,cmap='gray')
plt.subplot(133),plt.imshow(a2,cmap='gray')
plt.show()





