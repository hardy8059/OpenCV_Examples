import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut10/hist.png',0)
h_img = cv2.equalizeHist(img)
res = np.hstack((img,h_img))
cv2.imshow('Result',res)
cv2.waitKey(0)
