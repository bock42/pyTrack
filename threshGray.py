import cv2
import numpy

# set defaults
radPupil = [25,100]

img = cv2.imread('/home/abock/images/eye.png')
output = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

# blur the image
blur = cv2.GaussianBlur(thresh,(7,7),20)
# get the pupil
circlesPupil = cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT, 1, 10000,minRadius=radPupil[0],maxRadius=radPupil[1],param1=100,param2=10)

# ensure the pupil was found
if circlesPupil is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circlesPupil = numpy.round(circlesPupil[0, :]).astype("int")
 
	# draw the pupil 
	for (xP, yP, rP) in circlesPupil:
		cv2.circle(blur, (xP, yP), rP, (0, 255, 0), 4)
		radPupil = numpy.round([rP*0.85,rP*1.15]).astype("int")


cv2.imshow('image',blur)
cv2.waitKey(5000)
cv2.destroyAllWindows()



