import cv2
import numpy as np

img  = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut1/Messi.jpg')

ball = img[430:510,750:840]
#img[430:510,750:840]=[255,255,255]
img[430:510,600:690]=ball

cv2.imshow('image',img)

#img[0:0,60:60] = ball

cv2.waitKey(0)
