import cv2
import numpy as np
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)

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
        print "eyes:",eye
        for(ex,ey,ew,eh) in eye:
            grey = cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),[0,255,0],2)
            eyes = roi_color[ey:ey+ew,ex:ex+eh]
            egrey = cv2.cvtColor(eyes,cv2.COLOR_BGR2GRAY)

            _, thresholded = cv2.threshold(egrey, 30, 255, cv2.THRESH_BINARY,0)
            cv2.imshow('Thresh',thresholded)
            #plt.figure(figsize=(10, 5))
            #plt.imshow(thresholded, cmap='gray')

            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
            closed = cv2.erode(cv2.dilate(thresholded, kernel, iterations=1), kernel, iterations=1)

            #plt.figure(figsize=(10, 5))
            #plt.imshow(grey, cmap='gray')

            _,contours, hierarchy = cv2.findContours(closed, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

            drawing = np.copy(frame)

            for contour in contours:
                area = cv2.contourArea(contour)
                bounding_box = cv2.boundingRect(contour)
                radius = pow(area/3.14,0.5)
                extend = area / (bounding_box[2] * bounding_box[3])
                print extend
                # reject the contours with big extend
                if extend > 1.0:
                    continue

                # calculate countour center and draw a dot there
                m = cv2.moments(contour)
                if m['m00'] != 0:
                    center = (int(m['m10'] / m['m00']), int(m['m01'] / m['m00']))
                    cv2.circle(eyes, center, int(radius), [0, 255, 0], 3)

                # fit an ellipse around the contour and draw it into the image
            #ellipse = cv2.fitEllipse(contour)
            #drawing = cv2.ellipse(eyes,ellipse,[0, 255, 0],2)

    #plt.figure(figsize=(10, 5))
    #plt.show()
    cv2.imshow('Vids',frame)
    if(cv2.waitKey(5) &0xFF==ord('q')):
        break

cap.release()

