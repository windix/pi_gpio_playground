import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DS = 25
STCP = 23
SHCP = 24

GPIO.setup(DS, GPIO.OUT)
GPIO.setup(STCP, GPIO.OUT)
GPIO.setup(SHCP, GPIO.OUT)

dict = {
	#    A, B, C, D, E, F, G 	
	0: [ 1, 1, 1, 1, 1, 1, 0 ],
	1: [ 0, 1, 1, 0, 0, 0, 0 ],
	2: [ 1, 1, 0, 1, 1, 0, 1 ],
	3: [ 1, 1, 1, 1, 0, 0, 1 ],
	4: [ 0, 1, 1, 0, 0, 1, 1 ],
	5: [ 1, 0, 1, 1, 0, 1, 1 ],
	6: [ 1, 0, 1, 1, 1, 1, 1 ],
	7: [ 1, 1, 1, 0, 0, 0, 0 ],
	8: [ 1, 1, 1, 1, 1, 1, 1 ],
	9: [ 1, 1, 1, 1, 0, 1, 1 ],
	'clear': [ 0, 0, 0, 0, 0, 0, 0],
}

def set_bit_data(data):
	GPIO.output(DS, data)

	# make a up-shift (?) low -> high to output data
	GPIO.output(SHCP, 0)
	GPIO.output(SHCP, 1)


def show_digit(digit):
	print digit

	segs = dict[digit]
	
	set_bit_data(segs[6]) # G
	set_bit_data(segs[5]) # F
	set_bit_data(segs[4]) # E 
	set_bit_data(segs[3]) # D 
	set_bit_data(segs[2]) # C 
	set_bit_data(segs[1]) # B 
	set_bit_data(segs[0]) # A 

	# no decimal point
	set_bit_data(0)

	GPIO.output(STCP, 1)
	GPIO.output(STCP, 0)

for digit, segs in dict.iteritems():
	show_digit(digit)	
	time.sleep(0.2)

GPIO.cleanup()

