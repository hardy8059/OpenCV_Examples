import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/tut1/Messi.jpg',0)
rows,cols=img.shape

M_array = np.float32([[1,0,100],[0,1,50]])
res = cv2.warpAffine(img,M_array,(rows,cols))

cv2.imshow('shift',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
