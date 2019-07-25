import time
import picamera

camera = picamera.PiCamera()
#camera.capture('/home/pi/Desktop/camera/example.jpg')
camera.start_recording('/home/pi/Desktop/camera/examplevid.h264')
                       time.sleep(5) #5 seconds recording
                       camera.stop_recording
                       