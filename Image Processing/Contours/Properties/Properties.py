import cv2
import numpy as np

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut9/star.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

_,contours,_ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

cnt = contours[0]
########################################rectangle#####################################################
#x,y,w,h = cv2.boundingRect(cnt)
#res = cv2.rectangle(img,(x,y),(x+w,y+h),[0,255,0],2)
#ASPECT RATIO and extent
#print "Aspect Ratio",float(w)/h
#cArea = cv2.contourArea(cnt)
#rArea = float(w)*h
#Area = cArea/rArea
#print "Extent",cArea/Area
#hull  = cv2.convexHull(cnt)
#hArea = cv2.contourArea(hull)
#print "Solidity",float(cArea)/hArea
######################################fitting rectangle################################################
#rec = cv2.minAreaRect(cnt)
#box = cv2.boxPoints(rec)
#box = np.int0(box)
#res = cv2.drawContours(img,[box],0,[0,255,0],2)
#ASPECT RATIO and extent
#print "Aspect Ratio",float(w)/h
#cArea = cv2.contourArea(cnt)
#rArea = float(w)*h
#Area = cArea/rArea
#print "Extent",cArea/Area
#hull  = cv2.convexHull(cnt)
#hArea = cv2.contourArea(hull)
#print "Solidity",float(cArea)/hArea

##########################################circle###########################################################
#(x,y),radius = cv2.minEnclosingCircle(cnt)
#centre = (int(x),int(y))
#radius = int(radius)
#res = cv2.circle(img,centre,radius,[0,255,0],2)
#cArea = cv2.contourArea(cnt)
#print "Equivalent Diameter",np.sqrt(4*cArea/np.pi)
##############################################Ellipse##################################################
ellipse = cv2.fitEllipse(cnt)
res = cv2.ellipse(img,ellipse,[0,255,0],2)

###############################################Line####################################################
#rows,cols = img.shape[:2]
#[vx,vy,x,y] = cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
#lefty = int((-x*vy/vx) + y)
#righty = int(((cols-x)*vy/vx)+y)
#res = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

mask = np.zeros(imgray.shape,np.uint8)
min_value,max_value,min_loc,max_loc = cv2.minMaxLoc(imgray,mask = mask)
mean = cv2.mean(imgray,mask = mask)
#cv2.drawContours(mask,[cnt],0,255,-1)
#pixelPoints = np.transpose(np.nonzero(mask))
#pixelPoints = cv2.findNonZero(mask)
#print pixelPoints

print "MIN AND MAX VALUE:",min_value,max_value
print "MIN AND MAX LOC:",min_loc,max_loc
print "MEAN",mean

leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

#l=[leftmost,rightmost,topmost,bottommost]
#res = cv2.drawContours(res,l,0,[0,0,255],2)

cv2.imshow('Image',res)
cv2.waitKey(0)
