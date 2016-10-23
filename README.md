# pyTrack
Toolbox for eye tracking using Python

### Requirements
numpy

OpenCV

### Installation on Ubuntu 
the following was installed on Ubuntu 16.04.1 LTS

OpenCV installation instructions 

http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html#linux-installation

```
# compiler
sudo apt-get install build-essential
# required
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
# optional
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

# Numpy (may be redundant from above)
pip install numpy

# Install OpenCV
cd /path/to/your/github/repos/
git clone https://github.com/jayrambhia/Install-OpenCV.git
cd ./Install-OpenCV/Ubuntu
chmod +x ./* 
./opencv_latest.sh
```
### Description of output
The main function in this toolbox is `detectCirclesMovie.py`, which will open a movie file containing raw images of a human eye. The function will identify, track, and display the pupil using the Hough transform. The script will also identify, track, and display the glint (refelection from the infrared camera), which is useful for determining the gaze direction of the eye. The frame, x, y, and radius values for the pupil and glint are output as columns within a text file.

### Example of raw image
![alt tag](https://cloud.githubusercontent.com/assets/6589737/19627621/ccdd9be8-9918-11e6-977d-61eb988845a1.jpeg)

## Example of tracked image
![alt tag](https://cloud.githubusercontent.com/assets/6589737/19627664/0b3cba1c-991a-11e6-9e3c-c3c1d96b0e72.jpeg)

### Example of raw and simultaneously tracked image
![alt_tag](https://cloud.githubusercontent.com/assets/6589737/19627648/8e76042a-9919-11e6-8448-a9421cacb777.jpeg)
