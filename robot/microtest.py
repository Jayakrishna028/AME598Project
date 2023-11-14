import RPi.GPIO as GPIO
import gpiozero as gpio
import time
GPIO.cleanup()
trigPin = 2
echoPin = 3

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin , GPIO.OUT)
GPIO.setup(echoPin , GPIO.IN)

while True:
    print("The main Program has started......")
    GPIO.output(trigPin, GPIO.LOW)
    time.sleep(2)
    GPIO.output(trigPin, GPIO.HIGH)
    start_time = time.time()
    time.sleep(0.00001)
    GPIO.output(trigPin, GPIO.LOW)
    print("the program reached near the while loop2")
    while GPIO.input(echoPin)==1:
        end_time = time.time()
        duration = end_time-start_time
        distance = round(duration*17150)
        print(f"Distance:{distance}cm")
    time.sleep(1)