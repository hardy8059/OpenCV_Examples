import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue=np.array([110,100,100])
    higher_blue = np.array([130,255,255])

    lower_red = np.array([-10,100,100])
    higher_red = np.array([10,255,255])


    lower_green = np.array([50,100,100])
    higher_green = np.array([70,255,255])


    mask_red = cv2.inRange(hsv,lower_red,higher_red)
    mask_blue = cv2.inRange(hsv,lower_blue,higher_blue)
    mask_green = cv2.inRange(hsv,lower_green,higher_green)

    res = cv2.bitwise_and(frame,frame,mask=mask_red)
    res1 = cv2.bitwise_and(frame,frame,mask=mask_blue)
    res2 = cv2.bitwise_and(frame,frame,mask=mask_green)

    temp = cv2.add(res1,res)
    final = cv2.add(temp,res2)

    cv2.imshow('frame',frame)
    cv2.imshow('track',final)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
