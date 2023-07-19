import cv2 as cv
import numpy as np
img = cv.imread("lena.png")
acc = cv.imread("image.png")

newImage = np.hstack((img[:, :256], acc[:, 256:]))
cv.imshow("Lena",img)
cv.imshow("Acc",acc)
cv.imshow("newImage",newImage)
cv.waitKey(0)
cv.destroyAllWindows()


