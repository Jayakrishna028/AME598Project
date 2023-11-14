import RPi.GPIO as GPIO
import time

#Setting Pin variables
trigPin = 2
echoPin = 3

#setup code 
print("Setting Pin Modes......")
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin , GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(echoPin , GPIO.IN)
print("Pin Modes Set.....")
time.sleep(5)

def main():
    while True:sudo apt-get install python3-dev python3-rpi.gpio
        GPIO.output(trigPin, GPIO.HIGH)
        start_time = time.time()
        time.sleep(0.00001)
        GPIO.output(trigPin, GPIO.LOW)
        while GPIO.input(echoPin) == 0:
            start_time = time.time()
        while GPIO.input(echoPin) == 1:
            echo_time = time.time()
            break
        duration = echo_time - start_time
        distance = (duration*34300)/2
        print(f"Distance: {distance}")
        time.sleep(1)
    GPIO.cleanup()


if __name__ == "__main__":
    main()
