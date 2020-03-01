```python

#configuring the camera in raspberypi
#sudo raspi-config < interfacing options < camera < yes < ok . and reboot
#sudo apt-get install python3-picamera

import picamera
import time

camera = picamera.PiCamera()
#fliping the photo
camera.vflip= True
#capturing a photo
camera.capture('example.jpg')

#recording a 10 sec video
camera.start_recording('examplevideo.h264')
time.sleep(10)
camera.stop_recording

#set up a camera that closes  when we are done
with picamera.PiCamera()  as camera:
    camera.resolution = (1280,720)
    camera.capture("example.jpg")

```