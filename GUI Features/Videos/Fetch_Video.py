import numpy as np
import cv2
cap = cv2.VideoCapture("C:\Users\Hardik\Documents\OpeCV\Tut2\tut2.avi")
while(True):
    ret,frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        print("Not Valid")
cap.release()
cv2.destroyAllWindows()
