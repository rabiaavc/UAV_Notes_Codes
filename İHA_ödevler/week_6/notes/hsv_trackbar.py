import cv2 as cv
import numpy as np
def nothing(a):
    pass
img = cv.imread("cicek.jpg")
cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars",640,300)
cv.createTrackbar("Hue Min","Trackbars",0,179,nothing)
cv.createTrackbar("Hue Max","Trackbars",179,179,nothing)
cv.createTrackbar("Satur Min","Trackbars",0,255,nothing)
cv.createTrackbar("Satur Max","Trackbars",255,255,nothing)
cv.createTrackbar("Value Min","Trackbars",0,255,nothing)
cv.createTrackbar("Value Max","Trackbars",255,255,nothing)

while True:
    img = cv.imread("cicek.jpg")
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv.getTrackbarPos("Satur Min","Trackbars")
    s_max = cv.getTrackbarPos("Satur Max","Trackbars")
    v_min = cv.getTrackbarPos("Value Min","Trackbars")
    v_max = cv.getTrackbarPos("Value Max","Trackbars")
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv.inRange(imgHSV,lower,upper)
    contours, hierarchy = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(imgHSV,contours,-1,(0,255,0),2)
    cv.imshow("Masked",mask)
    cv.imshow("Image",img)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break

cv.imshow("hsv",imgHSV)
cv.waitKey(0)
cv.destroyAllWindows()
