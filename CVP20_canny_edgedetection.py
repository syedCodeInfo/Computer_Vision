import cv2 as cv
import numpy as np
from  matplotlib import pyplot as plt

def nothing(x):
    pass


cv.namedWindow("Images")
tracker1 = cv.createTrackbar('thres1',"Images",10,200,nothing)
tracker2 = cv.createTrackbar('thres2',"Images",10,200,nothing)

#first step gaussian remove noise
# intentsity gradient
#non maximum suppression
#Double threshold the potential edgets
#edges tracking by hystersis
while True:
    img = cv.imread("lena.png", 0)
    thres1 = cv.getTrackbarPos("thres1","Images")
    thres2 = cv.getTrackbarPos("thres2", "Images")
    canny_Edge = cv.Canny(img,thres1,thres2)
    cv.imshow("cannyimg",canny_Edge)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()

