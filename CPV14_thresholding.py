import cv2 as cv

img = cv.imread("colorful_balls.jpg")
threshold_value = 50
_, thres = cv.threshold(img, threshold_value, 255, cv.THRESH_BINARY)
_, thres1 = cv.threshold(img, threshold_value, 255, cv.THRESH_BINARY_INV)
_, thres2 = cv.threshold(img, threshold_value, 255, cv.THRESH_TRUNC)
_, thres3 = cv.threshold(img, threshold_value, 255, cv.THRESH_TOZERO)
_, thres4 = cv.threshold(img, threshold_value, 255, cv.THRESH_TOZERO_INV)
 

cv.imshow("image", img)
cv.imshow("thres", thres)
cv.imshow("THRESH_BINARY_INV", thres1)
cv.imshow("THRESH_TRUNC", thres2)
cv.imshow("THRESH_TOZERO", thres3)
cv.imshow("THRESH_TOZERO_INV", thres4)
cv.waitKey(0)
cv.destroyAllWindows()
