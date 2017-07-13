import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut1/Messi.jpg')
cv2.imshow('image',img)
px = img[100,100,2]
print px

#img[100,100] = [255,255,255]
#print img[100,100]

img.itemset((100,100,1),100)
print img.item(100,100,0)

print img.shape
print img.size
print img.dtype

cv2.waitKey(0)
