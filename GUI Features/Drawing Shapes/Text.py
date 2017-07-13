import numpy as np
import cv2
img = np.zeros((512,512,3),np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,255),font,4,(0,255,255),2,cv2.LINE_AA)
cv2.imshow("Frame",img)
cv2.waitKey(0)
