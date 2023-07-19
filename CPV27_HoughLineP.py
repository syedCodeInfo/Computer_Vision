import cv2 as cv
import  numpy as np

lena_image = cv.imread("lena.png")
grey_img = cv.cvtColor(lena_image,cv.COLOR_BGR2GRAY)
edges = cv.Canny(grey_img,50,150,apertureSize=3)
lines = cv.HoughLines(edges,1,np.pi/180,200)
ll = cv.HoughLinesP(edges,1,np.pi/180,200,minLineLength=100,maxLineGap=10)
for line in ll:
    x1,y1,x2,y2 = line[0]
    cv.line(lena_image)
cv.imshow("edges",edges)

print(lines)


cv.imshow("Lena",lena_image)

cv.waitKey(0)
cv.destroyAllWindows()