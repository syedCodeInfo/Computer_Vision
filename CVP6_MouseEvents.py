import cv2 as cv
import numpy as np

def event_click(event,x,y,flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
        text = str(x)+', '+str(y)
        cv.putText(img,text,(x,y),font,.5,(255,0,200),3)
        cv.imshow('image',img)
    if event == cv.EVENT_RBUTTONDOWN:
        #getting the color channel from the image
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y, x, 2]
        font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
        text = str(blue) + ', ' + str(green)+ ', ' + str(red)
        cv.putText(img, text, (x, y), font, .5, (0, 0, 200), 1)
        cv.imshow('image', img)



img = np.zeros((512,512,3),np.uint8)
cv.imshow('image',img)

cv.setMouseCallback('image',event_click)
cv.waitKey(0)
cv.destroyAllWindows()

