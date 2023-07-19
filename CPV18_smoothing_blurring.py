import cv2 as cv
import numpy as np
from  matplotlib import pyplot as plt

img = cv.imread("lena.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25

dst = cv.filter2D(img,-1,kernel)
blur = cv.blur(img,(3,3))
gaussian = cv.GaussianBlur(img,(3,3),0)
median_blur = cv.medianBlur(img,3,)
bilateral = cv.bilateralFilter(img,9,75,75)


images = [img,dst,blur,gaussian,median_blur,bilateral]
title =["input image","2D convolution","blur","gaussian","median_blur","bilateral"]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()