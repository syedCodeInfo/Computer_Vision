
import cv2 as cv
import numpy as np

#img = cv.imread("image.png" ,1)
img = np.zeros([512,512,3],np.uint8)
img = cv.line(img ,(0 ,0) ,(252 ,252) ,(0 ,0 ,255) ,5)
img = cv.arrowedLine(img, (0 ,200) ,(252 ,252) ,(120 ,72 ,100) ,10)
img = cv.rectangle(img ,(0 ,300) ,(500 ,210) ,(0 ,200 ,200) ,-1)
#img = cv.circle(img ,(150,150) ,50 ,(0 ,255 ,0) ,-1),
font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
img = cv.putText(img,'Hello',(10,400),font,4,(0,255,0),5,cv.LINE_AA)
cv.imshow("image", img)
k = cv.waitKey(0)
cv.destroyAllWindows()
