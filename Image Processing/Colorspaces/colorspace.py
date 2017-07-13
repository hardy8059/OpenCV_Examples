import cv2
import numpy as np

flags = [i for i in dir(cv2) if i .startswith('COLOR_')]
print flags

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut1/Messi.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('HSV',hsv)
cv2.imshow('Gray',gray)
cv2.waitKey(0)
