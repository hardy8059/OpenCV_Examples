import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut5/Noise.jpg')

blur = cv2.blur(img,(5,5))

cv2.imshow('Original',img)
cv2.imshow('Blurred',blur)
cv2.waitKey(0)
