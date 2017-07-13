import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/tut1/Messi.jpg')
kernel = np.ones((5,5),np.float32)/25

dst = cv2.filter2D(img,-1,kernel)

cv2.imshow('Original',img)
cv2.imshow('Filtered',dst)

'''
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Filtered')
plt.xticks([]),plt.yticks([])

plt.show()
'''
cv2.waitKey(0)
