import cv2

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/tut1/Messi.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
res = cv2.warpAffine(img,M,(rows,cols))

cv2.imshow('ORIGINAL',img)
cv2.imshow('rotated',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
