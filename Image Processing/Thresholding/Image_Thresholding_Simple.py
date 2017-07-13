import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/tut4/threshold.png')

res,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
res,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
res,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
res,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
res,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

title=['Original','Binary','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()



#cv2.imshow('threshold',img)
#cv2.waitKey(0)
