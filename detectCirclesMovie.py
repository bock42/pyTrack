import cv2
import numpy
import math

# load the eye tracking video
cap = cv2.VideoCapture('/home/abock/videos/eyeMovie.mov')

# loop through the frames
while(cap.isOpened()):
	# get the frame, save output for later
    	ret, frame = cap.read()
	output = frame.copy();

	# convert to gray
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# blur the image
	blur = cv2.medianBlur(gray,7)

	# binarize
	ret,thresh = cv2.threshold(blur,200,255,cv2.THRESH_BINARY)

	# get the pupil
	circlesPupil = cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT, 1, 10000,minRadius=15,maxRadius=100,param1=100,param2=10)

	# get the glint
	circlesGlint = cv2.HoughCircles(thresh, cv2.cv.CV_HOUGH_GRADIENT, 1, 10000,minRadius=1,maxRadius=10,param1=100,param2=10)

	# ensure the pupil was found
	if circlesPupil is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circlesPupil = numpy.round(circlesPupil[0, :]).astype("int")
 
		# draw the pupil 
		for (xP, yP, rP) in circlesPupil:
			cv2.circle(output, (xP, yP), rP, (0, 255, 0), 4)

	# ensure the glint was found
	if circlesGlint is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circlesGlint = numpy.round(circlesGlint[0, :]).astype("int")
 
		# draw the glint
		for (xG, yG, rG) in circlesGlint:
			# only if glint is inside the pupil
			if math.sqrt( pow((xP - xG),2) + pow((yP - yG),2) ) < rP:
				cv2.circle(output, (xG, yG), rG, (0, 0, 255), 4)

	# show the output image
	#cv2.imshow("output", numpy.hstack([frame, output]))
	cv2.imshow('output',output)

	# quit movie if "q" is pressed
    	if cv2.waitKey(33) & 0xFF == ord('q'):
        	break

# close the windows
cap.release()
cv2.destroyAllWindows()


