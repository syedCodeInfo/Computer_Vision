import cv2 as cv
import numpy as np
img1 = cv.imread("image.png")
h,w,ch = img1.shape
img = np.zeros((h,w,ch),np.uint8)
img = cv.rectangle(img,(300,0),(500,550),(255,255,255),-1)

bit_and = cv.bitwise_and(img,img1)
bit_or = cv.bitwise_or(img,img1)
bit_xor =cv.bitwise_xor(img,img1)
bit_not = cv.bitwise_not(img1)


cv.imshow("input image",img)
cv.imshow("Second image",img1)
cv.imshow("Bitwise And Result",bit_and)
cv.imshow("Bitwise Or Result",bit_or)
cv.imshow("Bitwise xor Result",bit_xor)
cv.imshow("Bitwise Not Result",bit_not)
cv.waitKey(0)
cv.destroyAllWindows()