import  cv2 as cv
import numpy as np

def color_changer(x):
    print(x)
img = np.zeros((255,255,3),np.uint8)
cv.namedWindow('image')
cv.createTrackbar('B','image',0,255,color_changer)
cv.createTrackbar('G','image',0,255,color_changer)
cv.createTrackbar('R','image',0,255,color_changer)

while (1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k==27:
        break

    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')

    img[:] = [b,g,r]
cv.destroyAllWindows()