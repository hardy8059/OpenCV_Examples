import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/eye.jpg')

#cv2.imshow('Frame',image)
#cv2.waitKey(2000)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Frame',gray)
#cv2.waitKey(2000)
#plt.figure(figsize=(10, 5))
#plt.imshow(gray, cmap='gray')

retval, thresholded = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

#plt.figure(figsize=(10, 5))
#plt.imshow(thresholded, cmap='gray')
#cv2.imshow('Frame',thresholded)
#cv2.waitKey(2000)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
closed = cv2.erode(cv2.dilate(thresholded, kernel, iterations=1), kernel, iterations=1)

#cv2.imshow('Frame',closed)
#cv2.waitKey(2000)

_,contours, hierarchy = cv2.findContours(closed, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#drawing = np.copy(image)

for contour in contours:
    area = cv2.contourArea(contour)
    bounding_box = cv2.boundingRect(contour)

    extend = area / (bounding_box[2] * bounding_box[3])
    print extend
    # reject the contours with big extend
    if extend > 1.0:
        continue

    # calculate countour center and draw a dot there
    m = cv2.moments(contour)
    if m['m00'] != 0:
        center = (int(m['m10'] / m['m00']), int(m['m01'] / m['m00']))
        image = cv2.circle(image, center, 3, [0, 255, 0], -1)
        #cv2.imshow('Frame',image)
        #cv2.waitKey(2000)
    # fit an ellipse around the contour and draw it into the image
    ellipse = cv2.fitEllipse(contour)
    image = cv2.ellipse(image,ellipse,[0, 255, 0],2)
    #cv2.imshow('Frame',image)
    #cv2.waitKey(2000)
cv2.imshow('Frame',image)
cv2.waitKey(0)
