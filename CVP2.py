import cv2 as cv

cap = cv.VideoCapture(0);
fourCC = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("realtime.avi",fourCC,20.0,(640,480))
print(cap.isOpened())
while cap.isOpened():
    #ret true or false if the frame is available
    ret,frame = cap.read()
    if ret==True:
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        out.write(frame)
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        cv.imshow("Video Frame",gray)

        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()