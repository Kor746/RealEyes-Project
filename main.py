import serial
import speech_recognition as sr
import pyaudio
import os
import cv2

#start speech recognition
r = sr.Recognizer()
with sr.Microphone() as source:
    audio=r.listen(source)

txt = r.recognize_google(audio).lower().strip() + ""

# print("TEXT: "+txt)
# base_url = os.getcwd()
image = 'img.jpg'
config = 'yolov3.cfg'
weights = 'yolov3.weights'
classes = 'yolov3.txt'

if txt.contains('avoid'):
 	#Start serial communication with arduino
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    while True:
        print (ser.readline())
        
        if ser.readline():
           os.system("sudo fswebcam -p YUYV -d /dev/video0 -r 720*720 -s 20 --no-banner --set brightness=200% img.jpg")
           yolo_args = "sudo python3 yolo.py --image {} --config {} --weights {} --classes {}".format(image, config, weights, classes)
           os.system(yolo_args) # this will talk as well

elif txt.contains('word' | 'world'):
    os.system("sudo fswebcam -p YUYV -d /dev/video0 -r 1020*720 -s 20 --no-banner --set brightness=200%  world.jpg")
    yolo_world_args = "sudo python3 yoloWorld.py --image {} --config {} --weights {} --classes {}".format(image, config, weights, classes)
    os.system(yolo_world_args)
