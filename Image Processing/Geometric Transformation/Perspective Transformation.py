import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Hardik/Documents/OpeCV/tut1/Messi.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[200,100],[700,100],[200,400],[650,400]])
pts2 = np.float32([[0,0],[500,0],[0,500],[500,500]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(500,500))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(dst),plt.title('AffineTransformation')
plt.show()
