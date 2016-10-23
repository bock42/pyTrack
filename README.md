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

### Example of raw image
https://cloud.githubusercontent.com/assets/6589737/19627621/ccdd9be8-9918-11e6-977d-61eb988845a1.jpeg
