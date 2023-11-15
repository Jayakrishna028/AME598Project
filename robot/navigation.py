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

#read Data form ultrasonic data and returns the data
def ReadUltrasonic():
    distance = []
    for i in range(3):
        GPIO.output(trigPins[i], GPIO.HIGH)
        start_time = time.time()
        time.sleep(0.00001)
        GPIO.output(trigPins[i], GPIO.LOW)
        while GPIO.input(echoPins[i]) == 0:
            start_time = time.time()
        while GPIO.input(echoPins[i]) == 1:
            echo_time = time.time()
            break
        duration = echo_time - start_time
        distance.append((duration*34300)/2)
        print(f"Distance: {distance}")
    
    return distance

#move forward
def Fowrard():
    GPIO.output(LeftWheelPins1, 1)
    GPIO.output(LeftWheelPins2, 0)
    GPIO.output(RightWheelPins1, 1)
    GPIO.output(RightWheelPins2, 0)  
    time.sleep(0.1)

#reset the pins of motors
def reset():
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
    reset()

#turn Right and wait
def turnRight():
    GPIO.output(LeftWheelPins1, 0)
    GPIO.output(LeftWheelPins2, 1)
    GPIO.output(RightWheelPins1, 1)
    GPIO.output(RightWheelPins2, 0)
    time.sleep(1)
    reset()

def main():
    while True:
        SonicData = ReadUltrasonic()
        
        


if __name__ == "__main__":
    main()


