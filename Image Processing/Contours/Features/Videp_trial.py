import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read()
    cv2.namedWindow('Thresh')
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    _,contours,_ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    cnt = contours[0]
    x,y,w,h = cv2.boundingRect(cnt)
    res = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Image',res)
    cv2.imshow('Thresh',thresh)

    if(cv2.waitKey(1)==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
