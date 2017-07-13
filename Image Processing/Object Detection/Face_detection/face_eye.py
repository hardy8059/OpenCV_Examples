import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut10/face1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.2,3,minSize = (500,500))
for (x,y,w,h) in faces :
    img = cv2.rectangle(img,(x,y),(x+w,y+h),[0,255,0],2)
    roi_color = img[y:y+h,x:x+w]
    roi_gray = gray[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray,1.1,3,minSize = (30,30))
    print eyes
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),[255,0,0],2,)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
