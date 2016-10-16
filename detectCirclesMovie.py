import cv2
import numpy

cap = cv2.VideoCapture('/home/abock/videos/eyeMovie.mov')

while(cap.isOpened()):
    	ret, frame = cap.read()
	
	output = frame.copy();

    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	blur = cv2.medianBlur(gray,7)

	ret,thresh = cv2.threshold(blur,200,255,cv2.THRESH_BINARY)

	circlesPupil = cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT, 1, 10000,minRadius=15,maxRadius=100,param1=100,param2=10)

	circlesGlint = cv2.HoughCircles(thresh, cv2.cv.CV_HOUGH_GRADIENT, 1, 10000,minRadius=1,maxRadius=10,param1=100,param2=10)

	# ensure at least some circles were found
	if circlesPupil is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circlesPupil = numpy.round(circlesPupil[0, :]).astype("int")
 
		# loop over the (x, y) coordinates and radius of the circles
		for (x, y, r) in circlesPupil:
			# draw the circle in the output image, then draw a rectangle
			# corresponding to the center of the circle
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			#cv2.circle(output, (x, y), 1, (0, 128, 255), -1)
			#cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0, 128, 255), -1)

	# ensure at least some circles were found
	if circlesGlint is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circlesGlint = numpy.round(circlesGlint[0, :]).astype("int")
 
		# loop over the (x, y) coordinates and radius of the circles
		for (x, y, r) in circlesGlint:
			# draw the circle in the output image, then draw a rectangle
			# corresponding to the center of the circle
			cv2.circle(output, (x, y), r, (0, 0, 255), 4)
			#cv2.circle(output, (x, y), 1, (0, 128, 255), -1)
			#cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0, 128, 255), -1)

	# show the output image
	#cv2.imshow("output", numpy.hstack([frame, output]))
	cv2.imshow('output',output)


    	if cv2.waitKey(33) & 0xFF == ord('q'):
        	break
cap.release()
cv2.destroyAllWindows()


