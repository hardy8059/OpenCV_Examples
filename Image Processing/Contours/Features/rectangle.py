import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/insect.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

_,contours,_ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

cnt = contours[0]
########################################rectangle#####################################################
#x,y,w,h = cv2.boundingRect(cnt)
#res = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

######################################fitting rectangle################################################
#rec = cv2.minAreaRect(cnt)
#box = cv2.boxPoints(rec)
#box = np.int0(box)
#res = cv2.drawContours(img,[box],0,(0,255,0),2)

##########################################circle###########################################################
#(x,y),radius = cv2.minEnclosingCircle(cnt)
#centre = (int(x),int(y))
#radius = int(radius)
#res = cv2.circle(img,centre,radius,(0,255,0),2)

##############################################Ellipse##################################################
#ellipse = cv2.fitEllipse(cnt)
#res = cv2.ellipse(img,ellipse,(0,255,0),2)

###############################################Line####################################################
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
res = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

cv2.imshow('Image',res)
cv2.waitKey(0)
