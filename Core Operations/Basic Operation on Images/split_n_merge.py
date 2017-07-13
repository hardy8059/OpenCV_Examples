import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut1/Messi.jpg')
b,g,r=cv2.split(img)
cv2.imshow('image',b)
cv2.waitKey(1000)
cv2.imshow('image1',g)
cv2.waitKey(1000)
cv2.imshow('image2',r)
cv2.waitKey(1000)
cv2.imshow('red',cv2.merge((r,g,b)))
cv2.waitKey(1000)
cv2.imshow('Green',cv2.merge((g,b,r)))
cv2.waitKey(1000)
cv2.imshow('Original',cv2.merge((b,g,r)))


cv2.waitKey(0)
