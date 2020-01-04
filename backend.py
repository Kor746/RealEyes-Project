# from upm import pyupm_grove as pyupm_grove
import os
import speech_recognition as sr


# r = sr.Recognizer()
#
# with sr.Microphone() as source:
#     audio = r.listen(source)

img_file_dir = os.getcwd() + 'assets/'
if not os.path.exists(img_file_dir):
    os.mkdir(img_file_dir)

# get image from camera and put it in format method

file_name = 'assets/{}'.format("temp_img")
img_file = os.getcwd() + file_name
# button = grove.GroveButton(27)
# if button.value() == 1:
while 1:
# try:
    image = 'chair.jpg'
    config = 'yolov3.cfg'
    weights = 'yolov3.weights'
    classes = 'yolov3.txt'
    # ultrasonic
    # object_distance =
    # speech to text

    # speech = r.recognize_google(audio).lower().strip()
    if 'detection' in ['collision', 'detection']:#speech
        # if object_distance <= 200:
        if True:
            arguments = "python3 yolo_impl.py --image {} --config {} --weights {} --classes {}".format(image, config, weights, classes)
            print(arguments)
            os.system(arguments)
            # ultrasonicYolo()

        # elif ['describe', 'world',] in speech:
            # worldYolo()
            # cropped_image = trim_image()
            # collisionYolo(cropped_image)
    # except Exception as err:
    #     print(err)
    # except sr.unknownValueError:
        # print("Cannot understand audio")
    # except sr.RequestError as e:
        # print("Could not request results from Google SPech Recognition")

        # if button.value() == 0:
        #     # Kill device
        #     break;
