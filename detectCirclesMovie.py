import cv2
import numpy
import math

# set defaults
radP = [25,100]
radG = [3,10]
p1P = 500
p1G = 500
p2P = 35
p2G = 10
maxp2P = 45

# load the eye tracking video
cap = cv2.VideoCapture('/home/abock/videos/eyeMovie.mov')

# loop through the frames
while(cap.isOpened()):
	# get the frame, save output for later
    	ret, frame = cap.read()
	output = frame.copy();

	# convert to gray
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# binarize
	ret,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

	# blur the image
	blur = cv2.GaussianBlur(thresh,(7,7),20)

	# get the pupil
	circlesPupil = cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT, 1, 10000,minRadius=radP[0],maxRadius=radP[1],param1=p1P,param2=p2P)

	# get the glint
	circlesGlint = cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT, 1, 10000,minRadius=radG[0],maxRadius=radG[1],param1=p1G,param2=p2G)

	# ensure the pupil was found
	if circlesPupil is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circlesPupil = numpy.round(circlesPupil[0, :]).astype("int")
		if p2P < maxp2P:
			p2P = numpy.round(p2P*1.05).astype("int")
 
		# draw the pupil 
		for (xP, yP, rP) in circlesPupil:
			cv2.circle(output, (xP, yP), rP, (0, 255, 0), 4)
			radP = numpy.round([rP*0.85,rP*1.15]).astype("int")

		# ensure the glint was found
		if circlesGlint is not None:
			# convert the (x, y) coordinates and radius of the circles to integers
			circlesGlint = numpy.round(circlesGlint[0, :]).astype("int")
 
			# draw the glint
			for (xG, yG, rG) in circlesGlint:
				# only if glint is inside the pupil
				if math.sqrt( pow((xP - xG),2) + pow((yP - yG),2) ) < rP:
					cv2.circle(output, (xG, yG), rG, (0, 0, 255), 4)
	else:
		# lower the param2 threshold
		p2P = numpy.round(p2P*0.95).astype("int")

	# show the output image
	cv2.imshow("output", numpy.hstack([frame, output]))
	#cv2.imshow('output',output)

	# quit movie if "q" is pressed
    	if cv2.waitKey(33) & 0xFF == ord('q'):
        	break

# close the windows
cap.release()
cv2.destroyAllWindows()


