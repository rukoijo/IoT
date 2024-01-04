# program to test if picture contains a face, if not face turn red led on  GPIO17 on if 
# face turn green led on GPIO18 on Raspberry Pi


import boto3
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED

import boto3
import json

def detect_faces(target_file, region):

    client=boto3.client('rekognition', region_name=region)

    imageTarget = open(target_file, 'rb')

    response = client.detect_faces(Image={'Bytes': imageTarget.read()}, 
    Attributes=['ALL'])

    print('Detected faces for ' + photo)
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))

        # Access predictions for individual face details and print them
        print("Gender: " + str(faceDetail['Gender']))
        print("Smile: " + str(faceDetail['Smile']))
        print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
        print("Emotions: " + str(faceDetail['Emotions'][0]))

    return len(response['FaceDetails'])

photo = 'jo.jpg'
region = 'us-east-1'
face_count=detect_faces(photo, region)
print("Faces detected: " + str(face_count))

if face_count == 1:
    print("Image suitable for use in collection.")
    # blink green led 10 times
    led = LED(18)
    for i in range(10):
        led.on()
        sleep(1)
        led.off()
        sleep(1)
else:
    print("Please submit an image with only one face.")
    # blink red led 10 times
    led = LED(17)
    for i in range(10):
        led.on()
        sleep(1)
        led.off()
        sleep(1)

