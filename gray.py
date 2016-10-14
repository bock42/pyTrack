import cv2
import numpy

#Read Image
img = cv2.imread('/home/abock/images/cat.jpeg')
#Display Image
cv2.imshow('image',img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#Applying Grayscale filter to image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Saving filtered image to new file
cv2.imwrite('/home/abock/images/graycat.jpeg',gray)
