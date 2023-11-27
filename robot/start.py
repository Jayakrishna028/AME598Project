import navigation
import time
import Distance
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14 , GPIO.OUT)
GPIO.setup(15 , GPIO.IN)

while True:
    distanceFront = Distance.distance(14 , 15)
    print(f"{distanceFront} > {time.time()}" )
    time.sleep(0.5)


GPIO.cleanup()