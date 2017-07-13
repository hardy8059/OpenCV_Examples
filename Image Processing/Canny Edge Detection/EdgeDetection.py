import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut1/Messi.jpg',0)

res = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap='gray'),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(res,cmap='gray'),plt.title('Edges')
plt.xticks([]),plt.yticks([])

plt.show()
