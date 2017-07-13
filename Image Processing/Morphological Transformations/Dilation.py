import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut6/binary.png')
kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(img,kernel,iterations = 5)

cv2.imshow('Original',img)
cv2.imshow('Kernel',kernel)
cv2.imshow('Blurred',dilation)
cv2.waitKey(0)
