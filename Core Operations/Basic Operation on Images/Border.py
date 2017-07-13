import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut1/Messi.jpg')
YELLOW = [255,0,0]

replicate = cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_REPLICATE)
reflect= cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_CONSTANT,value=YELLOW)

plt.subplot(231),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(232),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(233),plt.imshow(reflect_101,'gray'),plt.title('REFLECT 101')
plt.subplot(234),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(235),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
