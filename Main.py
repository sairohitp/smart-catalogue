import cv2 as cv

vid = cv.VideoCapture(0);

while(True):
    ret, frame = vid.read()
    cv.imshow('Window', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
