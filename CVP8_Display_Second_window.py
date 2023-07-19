import cv2 as cv
import numpy as np

def event_click(event,x,y,flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv.circle(img,(x,y),3,(0,255,0),-1)
        newImage = np.zeros((512,512,3),np.uint8)
        newImage[:] =[blue,green,red]
        cv.imshow('new Image', newImage)




#img = np.zeros((512,512,3),np.uint8)
img = cv.imread("image.png")
cv.imshow('image',img)
points = []
cv.setMouseCallback('image',event_click)
cv.waitKey(0)
cv.destroyAllWindows()

