import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read()

    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

 #   lower_blue=np.array([110,50,50])
 #   higher_blue = np.array([130,255,255])

    lower_red = np.array([-10,100,100])
    higher_red = np.array([10,255,255])


#    lower_green = np.array([50,50,50])
#    higher_green = np.array([70,255,255])

#   mask = cv2.inRange(hsv_frame,lower_blue,higher_blue)
    mask = cv2.inRange(hsv_frame,lower_red,higher_red)
#    mask = cv2.inRange(hsv_frame,lower_green,higher_green)
#    mask_inv = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('tracking',res)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
