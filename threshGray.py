import cv2
import numpy

img = cv2.imread('/home/abock/images/eye.png')
output = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)



