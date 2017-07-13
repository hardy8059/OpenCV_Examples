import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read()
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)

    image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    hull = cv2.convexHull(contours[0])

    res = cv2.drawContours(frame,hull,-1,(0,255,0),3)

    cv2.imshow('Image',res)

    if(cv2.waitKey(1)==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
