import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
right_button = 15
left_button = 14

GPIO.setup(led, GPIO.OUT)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)


GPIO.output(led, 1)

time.sleep(2)

GPIO.output(led, 0)

while True:
	if GPIO.input(left_button) == False:
		print("Left (GP14) button pressed")
		break
	if GPIO.input(right_button) == False:
		print("Right (GP15) button pressed")
		break

GPIO.cleanup()

