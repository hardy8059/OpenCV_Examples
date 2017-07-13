import numpy as np
import cv2
img = np.zeros((512,512,3),np.uint8)
cv2.circle(img,(250,250),90,(0,0,255),5)
cv2.imshow("Frame",img)
cv2.waitKey(0)
