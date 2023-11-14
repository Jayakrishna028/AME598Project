import RPi.GPIO as GPIO
import time
GPIO.cleanup()
backRightSig1 = 2
backRightSig2 = 3
backLeftSig1 = 4
backLeftSig2 = 17

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(backRightSig1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(backRightSig2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(backLeftSig1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(backLeftSig2, GPIO.OUT, initial = GPIO.LOW)

#time delay
time.sleep(1)
start_time = time.time()
current = time.time()
while current < start_time+10:
    GPIO.output(backLeftSig1, GPIO.HIGH)
    GPIO.output(backRightSig1, GPIO.HIGH)
    GPIO.output(backLeftSig2, GPIO.LOW)
    GPIO.output(backRightSig2, GPIO.LOW)
    
    