import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM) 
GPIO_TRIG = 2 
GPIO_ECHO = 3

#SETUP of the pins
GPIO.setup(GPIO_TRIG, GPIO.OUT, initial = GPIO.LOW) 
GPIO.setup(GPIO_ECHO, GPIO.IN) 


while True:
    time.sleep(2) 
    GPIO.output(GPIO_TRIG, GPIO.HIGH) 
    time.sleep(0.00001) 
    GPIO.output(GPIO_TRIG, GPIO.LOW) 
    while GPIO.input(GPIO_ECHO)==0: 
        start_time = time.time() 
    while GPIO.input(GPIO_ECHO)==1: 
        Bounce_back_time = time.time() 
        pulse_duration = Bounce_back_time - start_time 
        distance = round(pulse_duration * 17150, 2) 
        print (f"Distance: {distance} cm") 
GPIO.cleanup() 