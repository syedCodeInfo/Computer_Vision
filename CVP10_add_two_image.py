import cv2 as cv


img = cv.imread("image.png")
img1 = cv.imread("image2.png")
img = cv.resize(img,(300,300))
img1 = cv.resize(img1,(300,300))
dest = cv.add(img,img1)
des = cv.addWeighted(img,0.8,img1,0.2,0)
cv.imshow("Final Image",des)
cv.waitKey(0)
cv.destroyAllWindows()

#add Weight
