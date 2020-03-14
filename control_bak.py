import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(3)  # turn left
        time.sleep(0.5) # sleep 1 second

        p.ChangeDutyCycle(4)  # turn towards 90 degree
        time.sleep(0.5) # sleep 1 second

        p.ChangeDutyCycle(5) # turn right
        time.sleep(0.5) # sleep 1 second
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
