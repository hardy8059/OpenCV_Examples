import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut6/Noise.jpg')
kernel = np.ones((5,5),np.uint8)

opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

cv2.imshow('Original',img)
cv2.imshow('Filtered',opening)
cv2.waitKey(0)
