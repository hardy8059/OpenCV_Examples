import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/hand.jpg')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)

image,contours,hierarchy = cv2.findContours(thresh,1,2)

cnt = contours[4]

hull = cv2.convexHull(cnt)
print hull
res = cv2.drawContours(img,[hull],-1,(0,255,0),3)

cv2.imshow('Image',res)
cv2.waitKey(0)
