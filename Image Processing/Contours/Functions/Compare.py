import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/star.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_,contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
img2 = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/star2.jpg')
imgray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,thresh2 = cv2.threshold(imgray2,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_,contours2,_ = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
img3 = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/circle.jpg')
imgray3 = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret,thresh3 = cv2.threshold(imgray3,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_,contours3,_ = cv2.findContours(thresh3,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cnt = contours[0]
cnt2 = contours2[0]
cnt3 =  contours3[0]

ret  =cv2.matchShapes(cnt,cnt2,1,0.0)
ret1  =cv2.matchShapes(cnt,cnt3,1,0.0)

print "STAR TO EDITED STAR:",ret
print "STAR TO CIRCLE:",ret1
