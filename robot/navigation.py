import RPi.GPIO as GPIO
import time

LeftWheelPins1 = 2
LeftWheelPins2 = 3
RightWheelPins1 =4
RightWheelPins2 =17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LeftWheelPins1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LeftWheelPins2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(RightWheelPins1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(RightWheelPins2, GPIO.OUT, initial = GPIO.LOW)

pwm_LeftWheelPins1 = GPIO.PWM(LeftWheelPins1, 1000)  # Set frequency to 1 kHz
pwm_LeftWheelPins2 = GPIO.PWM(LeftWheelPins2, 1000)  
pwm_RightWheelPins1 = GPIO.PWM(RightWheelPins1, 1000)  
pwm_RightWheelPins2 = GPIO.PWM(RightWheelPins2, 1000)  

pwm_LeftWheelPins1.start(0)
pwm_LeftWheelPins2.start(0)
pwm_RightWheelPins1.start(0)
pwm_RightWheelPins2.start(0)

def Forward():
    pwm_LeftWheelPins1.ChangeDutyCycle(75)  
    pwm_LeftWheelPins2.ChangeDutyCycle(0)
    pwm_RightWheelPins1.ChangeDutyCycle(75)  
    pwm_RightWheelPins2.ChangeDutyCycle(0)
    time.sleep(0.1)


def stop():
    pwm_LeftWheelPins1.ChangeDutyCycle(0)
    pwm_LeftWheelPins2.ChangeDutyCycle(0)
    pwm_RightWheelPins1.ChangeDutyCycle(0)
    pwm_RightWheelPins2.ChangeDutyCycle(0)
    time.sleep(0.1) 

def turnLeft():
    pwm_LeftWheelPins1.ChangeDutyCycle(0)
    pwm_LeftWheelPins2.ChangeDutyCycle(0)
    pwm_RightWheelPins1.ChangeDutyCycle(100) 
    pwm_RightWheelPins2.ChangeDutyCycle(0)
    time.sleep(1)
    stop()


def turnRight():
    pwm_LeftWheelPins1.ChangeDutyCycle(100) 
    pwm_LeftWheelPins2.ChangeDutyCycle(0)
    pwm_RightWheelPins1.ChangeDutyCycle(0)
    pwm_RightWheelPins2.ChangeDutyCycle(0)
    time.sleep(1)
    stop()

def back():
    pwm_LeftWheelPins1.ChangeDutyCycle(0)
    pwm_LeftWheelPins2.ChangeDutyCycle(75)  
    pwm_RightWheelPins1.ChangeDutyCycle(0)
    pwm_RightWheelPins2.ChangeDutyCycle(75)  
    time.sleep(1)

        



