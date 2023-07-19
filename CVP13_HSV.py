import  cv2 as cv
import numpy as np

def color_changer(x):
    print(x)

cap = cv.VideoCapture(0)

cv.namedWindow("Tracking")
cv.createTrackbar("LH","Tracking",0,255,color_changer)
cv.createTrackbar("LS","Tracking",0,255,color_changer)
cv.createTrackbar("LV","Tracking",0,255,color_changer)
cv.createTrackbar("UH","Tracking",255,255,color_changer)
cv.createTrackbar("US","Tracking",255,255,color_changer)
cv.createTrackbar("UV","Tracking",255,255,color_changer)
while True:
    _,img  = cap.read()
    hsv_color = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    lh = cv.getTrackbarPos("LH","Tracking")
    ls = cv.getTrackbarPos("LS", "Tracking")
    lv = cv.getTrackbarPos("LV", "Tracking")

    uh = cv.getTrackbarPos("UH", "Tracking")
    us = cv.getTrackbarPos("US", "Tracking")
    uv = cv.getTrackbarPos("UV", "Tracking")

    lower_color_range = np.array([lh,ls,lv])
    higher_color_range = np.array([uh, us, uv])
    mask = cv.inRange(hsv_color,lower_color_range,higher_color_range)

    res= cv.bitwise_and(img,img, mask=mask)

    print(res)
    cv.imshow('image',img)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    cv.rectangle(res)
    cv.imshow('hsv image', hsv_color)
    k = cv.waitKey(1) & 0xFF
    if k==27:
        break

cv.destroyAllWindows()