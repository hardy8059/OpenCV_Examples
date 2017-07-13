import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut5/Median.jpg')

median = cv2.medianBlur(img,5)

cv2.imshow('Original',img)
cv2.imshow('Blurred',median)
cv2.waitKey(0)
