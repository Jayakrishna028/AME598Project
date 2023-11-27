import RPi.GPIO as GPIO
import time

RightSig1 = 2
RightSig2 = 3
LeftSig1 = 4
LeftSig2 = 17

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RightSig1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(RightSig2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LeftSig1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LeftSig2, GPIO.OUT, initial = GPIO.LOW)

#time delay
time.sleep(1)
start_time = time.time()
current = time.time()
while current < start_time+10:
    print(time.time())
    GPIO.output(LeftSig1, GPIO.HIGH)
    GPIO.output(RightSig1, GPIO.HIGH)
    GPIO.output(LeftSig2, GPIO.LOW)
    GPIO.output(RightSig2, GPIO.LOW)
    
GPIO.cleanup()