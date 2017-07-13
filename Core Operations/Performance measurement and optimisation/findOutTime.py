import cv2
import numpy as np

a=["\img3","\img2","\img3","\img4"]
images = np.array(a)

path="C:\Users\Hardik\Documents\OpeCV\Tut3"

i=0
while(1):
    t1=cv2.getTickCount()
    if(i!=3):
        img1 = path +  images[i] + '.jpg'
        img2 = path + images[i+1] + '.jpg'
        i=i+1
    elif(i==3):
        i=0

    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)

    cv2.imshow('SlideShow',image1)

    x=1.0
    while(x>0.0):
        dst = cv2.addWeighted(image1,x,image2,1.0-x,0)
        x=x-0.1
        cv2.imshow('SlideShow',dst)
    t2=cv2.getTickCount()
    k=cv2.waitKey(2000)
    if k==27:
        break

cv2.destroyAllWindows()

time=(t2-t1)/cv2.getTickFrequency()
print time

#OUTPUT:4.91333905611 for slide show
#OUTPUT:0.0115597066453 for one round of slideshow
