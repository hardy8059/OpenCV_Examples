import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/shape.png')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)

image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print contours

cnt = contours[0]

res = cv2.drawContours(img,cnt,-1,(0,255,0),13)
cv2.imshow("Image",res)
cv2.waitKey(0)
