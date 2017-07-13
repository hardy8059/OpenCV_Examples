import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut6/binary.png')
kernel = np.ones((5,5),np.uint8)

gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

cv2.imshow('Original',img)
cv2.imshow('Filtered',gradient)
cv2.waitKey(0)
