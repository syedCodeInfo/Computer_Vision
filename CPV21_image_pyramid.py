import cv2 as cv

img = cv.imread("lena.png")
lr = cv.pyrDown(img) # reduce the resolution of the image
ur = cv.pyrUp(img)
mena= cv.pyrMeanShiftFiltering(img,5,5)

cv.imshow("Original Image",img)
cv.imshow("pyrdown Image",lr)
cv.imshow("pyup Image",ur)
cv.imshow("mena Image",mena)
cv.waitKey(0)
cv.destroyAllWindows()