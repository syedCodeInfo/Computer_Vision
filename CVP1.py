'''Grey scale has 1 channel and color image has three channels. Numpy also installed along with the opencv. Numpy is used for numerical operation. images are 2d image pixcels
'''

import cv2 as cv

img = cv.imread("image.png", -1)
cv.imshow("image", img)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('p'):
    cv.imwrite("newImage.png", img)
    cv.destroyAllWindows()
