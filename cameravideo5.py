from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

for i in range(5):
    sleep(2)
    camera.start_recording('/home/pi/Desktop/videotest%s.h264' % i)
    sleep(5)
    camera.stop_recording()
camera.stop_preview()