import cv2
import numpy as np,sys

A = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut8/apple.jpg')
B = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut8/orange.jpg')

print A.size
print B.size

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(gpA[i])
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(gpB[i])
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in xrange(5,0,-1):
    size = (gpA[i-1].shape[1],gpA[i-1].shape[0])
    GE = cv2.pyrUp(gpA[i],dstsize = size)
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in xrange(5,0,-1):
    size = (gpA[i-1].shape[1],gpA[i-1].shape[0])
    GE = cv2.pyrUp(gpB[i],dstsize = size)
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in xrange(1,6):
    size = (LS[i].shape[1], LS[i].shape[0])
    ls_ = cv2.pyrUp(ls_,dstsize = size)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))


cv2.imshow('Pyramid blending',ls_)
cv2.imshow('Direct Blending',real)
cv2.waitKey(0)

