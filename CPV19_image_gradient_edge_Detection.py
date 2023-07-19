import cv2 as cv
import numpy as np
from  matplotlib import pyplot as plt

img = cv.imread("sudoku.png",0)
#gradient operations
#Laplican -- lapalican derviative
laplican = cv.Laplacian(img,cv.CV_64F,ksize=3)
print(laplican)
laplican = np.uint8(np.absolute(laplican))
#sobel dx = 0 order of derivative x and dy= order of derivative y


sobelX = cv.Sobel(img,cv.CV_64F,1,0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv.Sobel(img,cv.CV_64F,0,1)
sobelY = np.uint8(np.absolute(sobelY))
#sobel-y method
images = [img,laplican,sobelX,sobelY]
title =["input image","laplican","sobelX","sobelY"]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()