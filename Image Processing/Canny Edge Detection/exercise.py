import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut1/Messi.jpg',0)
cv2.namedWindow('Image')

cv2.createTrackbar('minValue','Image',0,500,nothing)
cv2.createTrackbar('maxValue','Image',0,500,nothing)
cv2.createTrackbar('switch','Image',0,1,nothing)

while(1):

    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break

    min = cv2.getTrackbarPos('minValue','Image')
    max = cv2.getTrackbarPos('maxValue','Image')
    s = cv2.getTrackbarPos('switch','Image')

    if s==0:
        img = img
        cv2.imshow('Image',img)
    elif s==1:
        res = cv2.Canny(img,min,max)
        cv2.imshow('Image',res)

cv2.destroyAllWindows()
