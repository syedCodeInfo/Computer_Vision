import cv2 as cv
import numpy as np

cap  = cv.VideoCapture("kitten.mp4")
ret,frame1 = cap.read()
ret,frame2 = cap.read()
while cap.isOpened():
    diff = cv.absdiff(frame1,frame2)
    grayFeed = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    #noise removal
    blur = cv.blur(grayFeed,(5,5),0)
    _,thres = cv.threshold(blur,20,255, cv.THRESH_BINARY)
    dilated = cv.dilate(thres,None, iterations=5)
    contours,_ = cv.findContours(dilated,cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for cont in contours:
        (x,y,w,h) = cv.boundingRect(cont)

        if cv.contourArea(cont)<8000:
            continue
        else:
            print(cv.contourArea(cont))
            cv.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
    #cv.drawContours(frame1,contours,-1,(0,255,0),2)
    cv.imshow("feed", frame1)

    cv.imshow("diff", diff)

    frame1 = frame2
    ret, frame2 = cap.read()


    if cv.waitKey(50)==27:
        break

cap.release()


