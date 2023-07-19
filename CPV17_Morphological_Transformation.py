import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("coin2.png",0)
_,mask = cv.threshold(img,127,255,cv.THRESH_BINARY)

kernal = np.ones((3,3),np.uint8)
dilation = cv.dilate(mask,kernal,iterations=2)
opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernal) # erosiion and followed by the dilation
erosion =cv.erode(mask,kernal,iterations=5)
closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernal)


titles = ["Input image","Mask","dilation","erosion","opening","closing"]
images = [img,mask,dilation,erosion,opening,closing]


for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()