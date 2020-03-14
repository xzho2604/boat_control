import RPi.GPIO as gpio
import time

def init_motor():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward():
    init_motor()
    gpio.output(11, True)
    gpio.output(15, False)
    #time.sleep(sec)
    #gpio.cleanup() # stop

def stop_motor():
    init_motor()
    gpio.output(11, False)
    gpio.output(15, False)

def stop_wheel():
    init_wheel()
    gpio.output(11, False)
    gpio.output(15, False)

def reverse():
    init_motor()
    gpio.output(11, False)
    gpio.output(15, True)


