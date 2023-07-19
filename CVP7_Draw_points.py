import cv2 as cv
import numpy as np

def event_click(event,x,y,flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv.line(img,points[-1],points[-2],(255,0,200),2)
            cv.imshow('image',img)




#img = np.zeros((512,512,3),np.uint8)
img = cv.imread("image.png")
cv.imshow('image',img)
points = []
cv.setMouseCallback('image',event_click)
cv.waitKey(0)
cv.destroyAllWindows()

