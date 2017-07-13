import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/tut1/Messi.jpg')
res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

cv2.imshow('ORIGIAL',img)
cv2.waitKey(2000)
cv2.imshow('Scaled',res)
cv2.waitKey(2000)
cv2.destroyAllWindows()

height,width=img.shape[:2]
res = cv2.resize(img,(2*height,2*width),interpolation=cv2.INTER_CUBIC)

cv2.imshow('ORIGIAL',img)
cv2.waitKey(2000)
cv2.imshow('Scaled',res)
cv2.waitKey(2000)
cv2.destroyAllWindows()
