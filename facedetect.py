import cv2
from cv2 import face
#Create a cascadeclassifier  object
face_cascade=cv2.CascadeClassifier("haarscade_frontaldace_default.xml")
img=cv2.imread('stev.jpg',1)
#Reading the image as gray scale image
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Search the co-ordinates of the image
faces=face_cascade.detectMultiScale(grey_img,scaleFactor=1.05,minNeighbors=5)
#print(type(faces))
print(faces)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#resized=cv2.resize(img,(int(img.shape[1]/7),int(img.shape[0]/7)))
cv2.imshow('Gray',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
