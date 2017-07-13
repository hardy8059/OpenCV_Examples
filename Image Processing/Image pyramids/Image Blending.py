import cv2
import numpy as np,sys

def blend(apple):
    G = apple.copy()
    gpA = [G]
    for i in xrange(6):
        G = cv2.pyrDown(gpA[i])
        gpA.append(G)

    lpA = [gpA[5]]
    for i in xrange(5,0,-1):
        size = (gpA[i-1].shape[1],gpA[i-1].shape[0])
        GE = cv2.pyrUp(gpA[i],dstsize = size)
        L = cv2.subtract(gpA[i-1],GE)
        lpA.append(L)
    return(lpA)

apple = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut8/apple.jpg')
orange = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut8/orange.jpg')

lpApple = blend(apple)
lpOrange = blend(orange)

LS=[]
for la,lb in zip(lpApple,lpOrange):
    rows,cols,dst = la.shape
    ls = np.hstack((la[:,:cols/2],lb[:,cols/2:]))
    LS.append(ls)

ls_=LS[0]
for i in xrange(1,6):
    size = (LS[i].shape[1], LS[i].shape[0])
    ls_=cv2.pyrUp(ls_,dstsize = size)
    ls_=cv2.add(ls_,LS[i])

real = np.hstack((apple[:,:cols/2],orange[:,cols/2:]))

cv2.imshow('Pyramid blending',ls_)
cv2.imshow('Direct Blending',real)
cv2.waitKey(0)
