import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut6/binary.png')
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)

cv2.imshow('Original',img)
cv2.imshow('Blurred',erosion)
cv2.waitKey(0)
