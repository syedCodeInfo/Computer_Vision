import cv2 as cv
import  numpy as np

lena_image = cv.imread("lena.png")
grey_img = cv.cvtColor(lena_image,cv.COLOR_BGR2GRAY)
edges = cv.Canny(grey_img,50,150,apertureSize=3)
lines = cv.HoughLines(edges,1,np.pi/180,200)
cv.imshow("edges",edges)




lena_face = cv.imread("lena_face.png",0)
h,w = lena_face.shape

temp_match = cv.matchTemplate(grey_img,lena_face,cv.TM_CCOEFF_NORMED)
print(temp_match)
threshold =0.9
loc = np.where(temp_match>=threshold)
print(loc)
for pt in zip(*loc):
    cv.rectangle(lena_image,pt,(pt[0]+h,pt[1]+w),(0,255,0),2)


cv.imshow("Lena",lena_image)
cv.imshow("Lena face",lena_face)
cv.waitKey(0)
cv.destroyAllWindows()