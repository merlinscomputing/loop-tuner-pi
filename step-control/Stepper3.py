import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 4 # pink
coil_A_2_pin = 17 # orange
coil_B_1_pin = 23 # blue
coil_B_2_pin = 24 # yellow
 
# adjust if different
StepCount = 8
Seq8 = range(0, StepCount)
Seq8[0] = [0,0,0,1]
Seq8[1] = [0,0,1,1]
Seq8[2] = [0,0,1,0]
Seq8[3] = [0,1,1,0]
Seq8[4] = [0,1,0,0]
Seq8[5] = [1,1,0,0]
Seq8[6] = [1,0,0,0]
Seq8[7] = [1,0,0,1]


Seq4 = range(0, 4) 
Seq4[0] = [1,0,1,0]
Seq4[1] = [0,1,1,0]
Seq4[2] = [0,1,0,1]
Seq4[3] = [1,0,0,1]
     
 
#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
#GPIO.output(enable_pin, 1)
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def forward_steps(delay, steps):
# loop through step sequence based on number of steps
	for i in range(0, steps):
	    setStep(1,0,1,0)
	    time.sleep(delay)
	    setStep(0,1,1,0)
	    time.sleep(delay)
	    setStep(0,1,0,1)
	    time.sleep(delay)
	    setStep(1,0,0,1)
	    time.sleep(delay)
	    
def forward_seq_steps(delay, steps):
# loop through step sequence based on number of steps
    seq=0
    for i in range(0, 25):
        print(seq)
        print(Seq4[seq])
        setStep(str(Seq4[seq]))
        time.sleep(delay)
        if seq<3:
            seq=seq+1
        else:
            seq=0

def forward_8_steps(delay, steps):
# loop through step sequence based on number of steps
	x=0
	for i in range(0, steps):
		setStep(Seq8[x])
        time.sleep(delay)
        if x<8:
            x=x+1
        else:
            x=0	    
    
def backward_steps(delay, steps):
# Reverse previous step sequence to reverse motor direction
    for i in range(0, steps):
	    setStep(1,0,0,1)
	    time.sleep(delay)
	    setStep(0,1,0,1)
	    time.sleep(delay)
	    setStep(0,1,1,0)
	    time.sleep(delay)
	    setStep(1,0,1,0)
	    time.sleep(delay)
	
def stop():
    setStep(0,0,0,0)



if __name__ == '__main__':
    while True:
        steps = raw_input("how many 4 steps?")
        #delay is forced to 50
        forward_seq_steps(int(5)/1000.0, int(steps))
        time.sleep(2)
        steps = raw_input("how many 8 steps?")
        backward_steps(int(5)/1000.0, int(steps))
        #delay is forced to 50
        #forward_8_steps(int(50)/1000.0, int(steps))
        stop()





