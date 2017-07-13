import cv2
import numpy as np

img1 = cv2.imread('C:\Users\Hardik\Documents\OpeCV\Tut1\Messi.jpg')
img2 = cv2.imread('C:\Users\Hardik\Documents\OpeCV\Tut3\img1.PNG')

#cv2.imshow('img1',img1)
#cv2.waitKey(2000)
#cv2.imshow('img2',img2)
#cv2.waitKey(2000)

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

#cv2.imshow('roi',roi)
#cv2.waitKey(2000)


img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,150,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

#cv2.imshow('img2ray',img2gray)
#cv2.waitKey(2000)

cv2.imshow('mask',mask)
cv2.waitKey(2000)

#cv2.imshow('mask_i',mask_inv)
#cv2.waitKey(2000)


print roi.size
print mask_inv.size
print img1.size
print mask.size

img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
cv2.imshow('img1_bg',mask)
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
cv2.imshow('img2_fg',mask_inv)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('Bitwise',img1)
cv2.waitKey(0)

cv2.destroyAllWindows()
