import cv2
import numpy
import math
import os

# set defaults
radP = [25,100]
radG = [3,10]
p1P = 500
p1G = 500
p2P = 35
p2G = 10
maxp2P = 45

# ask user for inputs
videoFile = input('Video file: ')
outDir = input('Output directory: ')
outFile = input('Output text file name: ')
if not os.path.exists(outDir):
    os.makedirs(outDir)

# load the eye tracking video
cap = cv2.VideoCapture(videoFile)

# save the output values
valFile = os.path.join(outDir,outFile)
with open(valFile,'w') as f:
    f.write(' '.join(["frame","xP","yP","rP","xG","yG","rG","\n"]))

# loop through the frames
xP = 0
yP = 0
rP = 0
xG = 0
yG = 0
rG = 0
ct = 0

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
    circlesPupil = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 10000,minRadius=radP[0],maxRadius=radP[1],param1=p1P,param2=p2P)

    # get the glint
    circlesGlint = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 10000,minRadius=radG[0],maxRadius=radG[1],param1=p1G,param2=p2G)
  
    # ensure the pupil was found
    if circlesPupil is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circlesPupil = numpy.round(circlesPupil[0, :]).astype("int")
        if p2P < maxp2P:
            p2P = numpy.round(p2P*1.01).astype("int")
          
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
        p2P = numpy.round(p2P*0.975).astype("int")
        radP = [25,100]
    
    # show the output image
    cv2.imshow("output", numpy.hstack([frame, output]))
    #cv2.imshow('output',output)

    # save the frames
    ct = ct + 1
    outFrame = os.path.join(outDir, "frame" + str(ct) + ".jpeg")
    cv2.imwrite(outFrame,numpy.hstack([frame, output]))
    #cv2.imwrite(outFrame,output)	
    
    with open(valFile,'a') as f:
        f.write(' '.join([str(ct),str(xP),str(yP),str(rP),str(xG),str(yG),str(rG),"\n"]))

    # quit movie if "q" is pressed
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# close the windows
cap.release()
cv2.destroyAllWindows()


