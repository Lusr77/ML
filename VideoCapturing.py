import cv2,time,pandas
from datetime import datetime
video=cv2.VideoCapture(0)
while 1:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing',gray)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
