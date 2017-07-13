import numpy as np
import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)

        if (cv2.waitKey(1) & 0xFF == ord('s')):
            print "Saved"
            out.write(frame)
        elif (cv2.waitKey(1) & 0xFF == ord('q')):
            break
        cv2.imshow('frame',frame)
cap.release()
out.release()
cv2.destroyAllWindows()


