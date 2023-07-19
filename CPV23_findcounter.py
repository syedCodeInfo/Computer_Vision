import cv2 as cv
import numpy as np
img = cv.imread("coins.jpg")
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
res,thres = cv.threshold(imgGray,127,255,0)
contours, hierachy = cv.findContours(thres,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(str(len(contours)))

cv.drawContours(img,contours,-1,(0,0,255),2)


cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()


