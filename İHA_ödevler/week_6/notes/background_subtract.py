import cv2 as cv

cap = cv.VideoCapture(0)

background_sub = cv.createBackgroundSubtractorMOG2() #ışığa duyarlı
bs = cv.createBackgroundSubtractorKNN()

while True:
    ret,frame = cap.read()
    mask = bs.apply(frame)
    mask = cv.medianBlur(mask,5)


    cv.imshow("mask",mask)
    cv.imshow("frame",frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.release()
cv.destroyAllWindows()