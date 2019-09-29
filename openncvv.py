import cv2
img=cv2.imread("stev.jpg",1)
print(img.shape)
print(img[0][0])
resized_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow('stev.jpg',resized_img)
cv2.imwrite('stev.jpg',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()