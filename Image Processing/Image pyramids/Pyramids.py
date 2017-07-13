import cv2


img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut1/Messi.jpg')
G = img.copy()
gpA = [G]
for i in xrange(3):
    G = cv2.pyrDown(gpA[i])
    gpA.append(G)
    cv2.imshow('Image',G)
    cv2.waitKey(2000)

lpA = [gpA[2]]
for i in range(2,0,-1):
    size=(gpA[i-1].shape[1],gpA[i-1].shape[0])
    GE = cv2.pyrUp(gpA[i],dstsize = size)
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)
    cv2.imshow('Image',L)
    cv2.waitKey(2000)

cv2.waitKey(0)
