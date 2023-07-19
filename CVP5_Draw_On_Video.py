import cv2 as cv
import datetime
cap = cv.VideoCapture(0)
date_time = datetime.datetime.utcnow()
while True:
    ret, frame = cap.read()
    if ret == True:
        font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
        text = 'Width:' + str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        frame = cv.putText(frame, str(date_time), (100, 100), font, 1, (0, 255, 0), 4,cv.LINE_AA)

        cv.imshow("Frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
