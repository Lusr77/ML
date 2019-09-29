import cv2,time
first_frame=0

video=cv2.VideoCapture(0)

while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('cap',gray)
