import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.start(7.5)

def boat_turn_left():
    p.ChangeDutyCycle(3)  # turn left

def boat_turn_right():
    p.ChangeDutyCycle(5)  # turn left

def boat_turn_middle():
    p.ChangeDutyCycle(4)  # turn left





