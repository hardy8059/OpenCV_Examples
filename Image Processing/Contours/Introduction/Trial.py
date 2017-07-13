import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read()
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(imgray,200,255,0)

    image,contour,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('gray',image)
    if(cv2.waitKey(1)==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
