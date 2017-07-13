import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/eye.jpg',0)
img = cv2.medianBlur(img,5)
c_img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=100,param2=50,minRadius=0,maxRadius=0)

for i in circles[0,:]:
    cv2.circle(c_img,(i[0],i[1]),i[2],[0,0,255],3)
    cv2.circle(c_img,(i[0],i[1]),2,[100,200,255],-1)

cv2.imshow('Circle',c_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
