import cv2 as cv
#threhold accept only grey scale image
img = cv.imread("sudoku.png",0)
threshold_value = 125
_, thres = cv.threshold(img, threshold_value, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

cv.imshow("image", img)
cv.imshow("thres", thres)
cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv.imshow("GAUSSIAN_C", th3)
cv.waitKey(0)
cv.destroyAllWindows()
