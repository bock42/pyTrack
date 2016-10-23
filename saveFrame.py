import cv2
import numpy
import os

outDir = '/home/abock/videos/Rawframes'
cap = cv2.VideoCapture('/home/abock/videos/eyeMovie.mov')

if not os.path.exists(outDir):
    os.makedirs(outDir)

ct = 0
while(cap.isOpened()):
	ret, frame = cap.read()
	
	ct = ct + 1

    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    	cv2.imshow('frame',gray)

	#Saving filtered image to new file
	outFrame = os.path.join(outDir, "frame" + str(ct) + ".jpeg")
	cv2.imwrite(outFrame,gray)

	# Break if 'q' is pressed	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
