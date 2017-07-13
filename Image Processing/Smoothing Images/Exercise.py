import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/Tut5/Noise.jpg')

average = cv2.blur(img,(5,5))
gaussian = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,9,75,75)

images = [img,average,gaussian,median,bilateral]
titles = ['Original','Average','Gaussian','Median','bilateral']

for i in xrange(5):
    plt.subplot(2,3,1+i),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
