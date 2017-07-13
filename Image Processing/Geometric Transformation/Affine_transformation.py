import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/tut1/Messi.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[400,100],[600,100],[200,700]])
pts2 = np.float32([[600,100],[200,500],[400,550]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(dst),plt.title('AffineTransforamtion')
plt.show()
