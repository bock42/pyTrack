# pyTrack
Toolbox for eye tracking using Python

### Example of raw and simultaneously tracked image
![alt_tag](https://cloud.githubusercontent.com/assets/6589737/19627648/8e76042a-9919-11e6-8448-a9421cacb777.jpeg)

### Requirements
numpy

OpenCV

### Installation on Ubuntu 
The following was installed on Ubuntu 16.04.1 LTS

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

### Installation on Mac
The following was installed on OSX 10.10.5 (Yosemite)

Install homebrew (http://brew.sh/) if not already installed

```
# Homebrew maintenance
brew doctor
brew update
brew upgrade

# Install OpenCV
brew tap homebrew/science
brew install opencv

# Install numpy
pip install numpy

# Add site-packages to path
export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
```
Note: the last line can be added to e.g. `~.bash_profile`


### Sample movie file
Download the file below to a local folder

https://drive.google.com/file/d/0B0H_0f12gCZvQ3M1Z1pxclZpMTA/view?usp=sharing

### Usage
The main function in this toolbox is `trackPupil.py`, which will open a movie file containing raw images of a human eye. The function will identify, track, and display the pupil using the Hough transform. The script will also identify, track, and display the glint (refelection from the infrared camera), which is useful for determining the gaze direction of the eye. The frames are saved as images, and the x, y, and radius values for the pupil and glint are output as columns within a text file.

The script will ask the user for the path to the input movie file, as well as the output directory and text file name.

For example:

```
$ python trackPupil.py
Video file: /homa/abock/videos/eyeMovie.mov
Output Directory: /home/abock/eyeTracking
Output text file name: eyeTracking.txt
```


### Example output file
```
frame xP yP rP xG yG rG 
1 416 258 55 408 254 9 
2 416 258 55 408 254 9 
3 416 258 55 408 254 9 
4 394 256 53 396 252 9 
5 394 254 51 396 252 9 
6 398 256 52 394 254 9 
7 394 260 53 396 252 9 
8 400 258 48 396 254 9 
9 400 258 48 396 254 9 
...
```

