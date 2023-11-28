import RPi.GPIO as GPIO
import time

LeftWheelPins1 = 2
LeftWheelPins2 = 3
RightWheelPins1 =4
RightWheelPins2 =17
trigPins = [14, 22, 23]
echoPins = [15, 27, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LeftWheelPins1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LeftWheelPins2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(RightWheelPins1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(RightWheelPins2, GPIO.OUT, initial = GPIO.LOW)

#move forward
def Forward():
    GPIO.output(LeftWheelPins1, 1)
    GPIO.output(LeftWheelPins2, 0)
    GPIO.output(RightWheelPins1, 1)
    GPIO.output(RightWheelPins2, 0)  
    time.sleep(0.1)

#reset the pins of motors
def stop():
    GPIO.output(LeftWheelPins1, 0)
    GPIO.output(LeftWheelPins2, 0)
    GPIO.output(RightWheelPins1, 0)
    GPIO.output(RightWheelPins2, 0)  
    time.sleep(0.1) 

#turn Left and wait
def turnLeft():

    GPIO.output(LeftWheelPins1, 1)
    GPIO.output(LeftWheelPins2, 0)
    GPIO.output(RightWheelPins1, 0)
    GPIO.output(RightWheelPins2, 1)
    time.sleep(1)
    stop()

#turn Right and wait
def turnRight():
    GPIO.output(LeftWheelPins1, 0)
    GPIO.output(LeftWheelPins2, 1)
    GPIO.output(RightWheelPins1, 1)
    GPIO.output(RightWheelPins2, 0)
    time.sleep(1)
    stop()
        



