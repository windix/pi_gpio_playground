import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

A = 4
B = 17
C = 27
D = 22
E = 18
F = 23
G = 25
DP = 10

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(DP, GPIO.OUT)

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
}

def show_digit(digit):
	print digit

	segs = dict[digit]
	
	GPIO.output(A, segs[0])
	GPIO.output(B, segs[1])
	GPIO.output(C, segs[2])
	GPIO.output(D, segs[3])
	GPIO.output(E, segs[4])
	GPIO.output(F, segs[5])
	GPIO.output(G, segs[6])

	return

# no decimal point
GPIO.output(DP, 0)

for digit, segs in dict.iteritems():
	show_digit(digit)	
	time.sleep(1)

GPIO.cleanup()


