import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut5/Noise.jpg')

bilateral = cv2.bilateralFilter(img,9,75,75)

cv2.imshow('Original',img)
cv2.imshow('Filtered',bilateral)
cv2.waitKey(0)
