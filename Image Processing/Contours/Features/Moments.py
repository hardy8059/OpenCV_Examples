import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/eye.jpg',0)

ret,thresh = cv2.threshold(img,127,255,0)

image, contours, hierarchy= cv2.findContours(thresh,1,2)

cnt = contours[0]

M = cv2.moments(cnt)
print M
print "Centroid:"
Cx = int(M['m10']/M['m00'])
Cy = int(M['m01']/M['m00'])
print Cx,Cy



