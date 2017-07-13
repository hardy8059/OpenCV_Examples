import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/shape.png')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)

image,contours,hierarchy = cv2.findContours(thresh,1,2)

cnt = contours[0]

epilson = 0.01*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epilson,True)

img = cv2.drawContours(img,[approx],-1,(255,255,0),2)

cv2.imshow("Image",img)
cv2.waitKey(0)
