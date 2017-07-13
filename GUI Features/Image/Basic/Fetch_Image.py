import cv2
img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut1/Messi.jpg',1)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('C:/Users/Hardik/Documents/OpeCV/Tut1/Messi.jpg',img)

