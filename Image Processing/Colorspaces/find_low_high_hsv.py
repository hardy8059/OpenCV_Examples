import cv2
import numpy as np

img = np.uint8([[[0,255,0]]])
print(cv2.cvtColor(img,cv2.COLOR_BGR2HSV))
cv2.waitKey(0)
