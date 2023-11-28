import RPi.GPIO as GPIO
import time
import Distance
import navigation
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

navigation.Forward()