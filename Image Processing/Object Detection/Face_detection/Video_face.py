import cv2
import numpy as np

cap = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(1):
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.2,3)
    #print faces
    for (x,y,w,h) in faces:
        #print "Rectangle"
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eye = eye_cascade.detectMultiScale(roi_gray,minSize = (30,30))
        for(ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),[0,255,0],2)
            #eye_frame = roi_color[ey:ey+eh,ex:ex+ew]
        #grayFrame = cv2.cvtColor(eye_frame,cv2.COLOR_BGR2GRAY)
        #grayFrame = cv2.medianBlur(grayFrame,5)
        #circles = cv2.HoughCircles(grayFrame,cv2.HOUGH_GRADIENT,1,50,param1=100,param2=50,minRadius=0,maxRadius=0)
        #print circles
        #for i in circles[0,:]:
        #    cv2.circle(roi_color,(i[0],i[1]),i[2],[0,0,255],-1)
        #    cv2.circle(roi_color,(i[0],i[1]),2,[100,200,255],-1)

    cv2.imshow('Live',frame)
    if(cv2.waitKey(5)==ord('q')):
        break

cap.release()

