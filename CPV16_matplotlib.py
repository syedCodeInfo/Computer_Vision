import cv2 as cv
from matplotlib import  pyplot as plt

#threhold accept only grey scale image
img = cv.imread("sudoku.png",0)
threshold_value = 125
_, thres = cv.threshold(img, threshold_value, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)




title = ["OrginalImage","Binary","Median","Gaussian"]
images = [img,thres,th2,th3]

for i in range(4):
    plt.subplots(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()
