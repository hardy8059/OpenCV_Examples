import numpy as np
import cv2
img = np.zeros((512,512,3),np.uint8)
arr = np.array([[100,50],[500,200],[200,300],[500,100]],np.int32)
arr = arr.reshape(-1,1,2)
cv2.polylines(img,[arr],True,(255,255,0))
cv2.imshow("Frame",img)
cv2.waitKey(0)
