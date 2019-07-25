import time
import picamera

camera = picamera.PiCamera()
camera.vflip = True
camera.capture('/home/pi/Desktop/camera/example.jpg')
