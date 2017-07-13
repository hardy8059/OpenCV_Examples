import numpy as np
import cv2
img = np.zeros((512,512,3),np.uint8)
cv2.rectangle(img,(0,0),(512,512),(255,255,255),-1)
cv2.ellipse(img,(256,148),(43,43),0,125,415,(0,0,255),-1)
cv2.ellipse(img,(200,230),(43,43),0,0,305,(0,255,0),-1)
cv2.ellipse(img,(310,230),(43,43),0,-415,-125,(255,0,0),-1)
cv2.circle(img,(256,148),15,(255,255,255),-1)
cv2.circle(img,(200,230),15,(255,255,255),-1)
cv2.circle(img,(310,230),15,(255,255,255),-1)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"OpenCV",(140,330),font,2,(0,0,0),2)
cv2.imshow("Exercise",img)
cv2.waitKey(0)
