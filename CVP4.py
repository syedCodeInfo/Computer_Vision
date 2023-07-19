import cv2 as cv

cap = cv.VideoCapture(0);
# change the resolution for the webcam
cap.set(3, 3000)
cap.set(4, 3000)
while cap.isOpened():
    # ret true or false if the frame is available
    ret, frame = cap.read()
    if ret == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        cv.imshow("Video Frame", gray)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()

cv.destroyAllWindows()
