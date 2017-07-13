import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/star.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_,contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cnt = contours[0]



rows= img.shape[0]
cols = img.shape[1]
print rows,cols

for i in range(rows):
    for j in range(cols):
        dst = cv2.pointPolygonTest(cnt,(i,j),True)
        if(dst < 0):
            img[i,j] = [235+dst,0,0]
        if(dst == 0):
            img[i,j] = [255,255,255]
        if(dst > 0):
            img[i,j] = [0,0,235-dst]


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
