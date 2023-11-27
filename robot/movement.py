import RPi.GPIO as GPIO
import time

RightSig1 = 2
RightSig2 = 3
LeftSig1 = 4
LeftSig2 = 17
en1 = 14
en2 = 15

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RightSig1, GPIO.OUT)
GPIO.setup(RightSig2, GPIO.OUT)
GPIO.setup(LeftSig1, GPIO.OUT)
GPIO.setup(LeftSig2, GPIO.OUT)
GPIO.setup(en1 , GPIO.OUT)
GPIO.setup(en2 , GPIO.OUT)
p1 = GPIO.PWM(en1, 1000)
p2 = GPIO.PWM(en2 , 1000)


#time delay
time.sleep(1)
p1.start(25)
p2.start(25)
start_time = time.time()
current = time.time()
while current < start_time+10:
    print(time.time())
    GPIO.output(LeftSig1, GPIO.HIGH)
    GPIO.output(RightSig1, GPIO.HIGH)
    GPIO.output(LeftSig2, GPIO.LOW)
    GPIO.output(RightSig2, GPIO.LOW)
    
GPIO.cleanup()