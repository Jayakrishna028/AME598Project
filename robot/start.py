import navigation
import time
import Distance
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#motor pins
RightSig1 = 2
RightSig2 = 3
LeftSig1 = 4
LeftSig2 = 17

#Ultrasonic pins

trigPin1 = 14
echoPin1 = 15
trigPin2 = 17
echoPin2 = 18
trigPin3 = 23
echoPin3 = 24

#setup for pins
GPIO.setup(RightSig1, GPIO.OUT)
GPIO.setup(RightSig2, GPIO.OUT)
GPIO.setup(LeftSig1, GPIO.OUT)
GPIO.setup(LeftSig2, GPIO.OUT)

#ultrasonic pins 
GPIO.setup(trigPin1 , GPIO.OUT)
GPIO.setup(echoPin1 , GPIO.IN)
GPIO.setup(trigPin2 , GPIO.OUT)
GPIO.setup(echoPin2 , GPIO.IN)
GPIO.setup(trigPin3 , GPIO.OUT)
GPIO.setup(echoPin3 , GPIO.IN)



navigation.Forward()


while True:
    distanceFront = Distance.distance(trigPin1 , echoPin1)
    # distanceRight = Distance.distance(trigPin2, echoPin2)
    # distanceLeft = Distance.distance(trigPin3 , echoPin3)
    print(distanceFront)
    # print(f"distance Front = {distanceFront}    Distance Right = {distanceRight}    Distance Left = {distanceLeft}" )
    time.sleep(0.5)



GPIO.cleanup()