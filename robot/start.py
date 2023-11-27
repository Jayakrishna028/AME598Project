import navigation
import Distance
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

distanceFront = Distance.distance(14 , 15)

while True:
    print(distanceFront)


GPIO.cleanup()