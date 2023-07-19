import cv2 as cv
import numpy as np

img = cv.imread("image.png")
cv.imshow('image',img)
print(img.shape) # return number of number of rows, columns and channels
print(img.size) # return total number of pixels accessed
print(img.dtype) # return image datatype
b,g,r = cv.split(img)
img1 = cv.merge((b,g,r))
myPoints =[]
def mouse_event(event,x,y, flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
        myPoints.append((x,y))
        if len(myPoints) == 2:
            cv.rectangle(img,myPoints[-1],myPoints[-2],(0,255,0),2)
            cv.imshow('image', img)
        elif len(myPoints)>2:
            print(myPoints)
            myNewImage = img[myPoints[0][1]:myPoints[1][1],myPoints[0][0]:myPoints[1][0]]
            height, width,ch = myNewImage.shape
            print(height,',',width)
            # Ensure that the region is within the bounds of img
            if y + height <= img.shape[0] and x+ width <= img.shape[1]:
                img[y:y + height, x:x + width] = myNewImage
            else:
                print("Region out of bounds")
        cv.imshow('image', img)


cv.setMouseCallback('image',mouse_event)
cv.waitKey(0) #q
cv.destroyAllWindows()
