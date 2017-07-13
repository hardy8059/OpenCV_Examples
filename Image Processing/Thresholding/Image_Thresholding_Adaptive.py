import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/tut4/sudoku.png',0)
img  = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,207,255,cv2.THRESH_BINARY)
th2  = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


title=['Original','Binary','MEAN','GAUSSIAN']
images=[img,th1,th2,th3]

for i in xrange(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
