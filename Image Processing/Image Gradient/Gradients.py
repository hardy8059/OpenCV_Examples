import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut7/sudoku.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobel = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 3)
scharr = cv2.Sobel(img,cv2.CV_64F,0,1,ksize = 5)

images=[img,laplacian,sobel,scharr]
titles=['ORIGINAL','LAPLACIAN','SOBEL','SCHARR']

for i in xrange(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
