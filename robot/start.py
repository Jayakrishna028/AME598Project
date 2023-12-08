
import navigation
import time
import Distance
from http_request import serverRequest
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#motor pins
RightSig1 = 2
RightSig2 = 3
LeftSig1 = 4
LeftSig2 = 17

#Ultrasonic pins

trigPin1 = 14
echoPin1 = 15
trigPin2 = 7
echoPin2 = 8
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

startTime = time.time()

while time.time() - startTime < 60:
    distanceFront = Distance.distance(trigPin1 , echoPin1)
    distanceRight = Distance.distance(trigPin2, echoPin2)
    distanceLeft = Distance.distance(trigPin3 , echoPin3)
    print(distanceFront ,distanceRight ,distanceLeft)
    navigation.Forward()
    serverRequest(distanceFront, distanceRight, distanceLeft)
    # print(f"{distanceFront} and {distanceLeft}")
    
    # # print(f"distance Front = {distanceFront}    Distance Right = {distanceRight}    Distance Left = {distanceLeft}" )
    time.sleep(0.5)

    if distanceFront > 30:
        navigation.Forward()
    elif distanceRight > 30:
        navigation.turnRight()
    elif distanceLeft > 30:
        navigation.turnLeft()
    else:
        navigation.back()
        navigation.turnRight()
        
navigation.stop()


GPIO.cleanup()