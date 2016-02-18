import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DS = 25
STCP = 23
SHCP = 24

D1 = 4
D2 = 17
D3 = 27
D4 = 22

GPIO.setup(DS, GPIO.OUT)
GPIO.setup(STCP, GPIO.OUT)
GPIO.setup(SHCP, GPIO.OUT)

GPIO.setup(D1, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(D3, GPIO.OUT)
GPIO.setup(D4, GPIO.OUT)
	
GPIO.output(D1, 1)
GPIO.output(D2, 1)
GPIO.output(D3, 1)
GPIO.output(D4, 1)

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


def show_digit(digit, pos):
	print digit, pos

	if (pos == 0): GPIO.output(D4, 0)
	if (pos == 1): GPIO.output(D3, 0)
	if (pos == 2): GPIO.output(D2, 0)
	if (pos == 3): GPIO.output(D1, 0)

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


for d in range(0, 12):
	if d < 10:
		#print d, 0
		show_digit(d, 0)
		time.sleep(0.2)

	elif d < 100:
		print "[", d, "]"
		#print d % 10, 0
		#print d / 10, 1
		show_digit(d % 10, 0)
		show_digit(d / 10, 1)
		time.sleep(0.2)

show_digit('clear', 0)
show_digit('clear', 1)
show_digit('clear', 2)
show_digit('clear', 3)

GPIO.cleanup()

