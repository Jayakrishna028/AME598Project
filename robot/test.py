import RPi.GPIO as GPIO
import time
import Distance

trigPin1 = 14
echoPin1 = 15

GPIO.setup(trigPin1 , GPIO.OUT)
GPIO.setup(echoPin1 , GPIO.IN)

distance1 = Distance.distance(trigPin1 , echoPin1)
print(distance1)