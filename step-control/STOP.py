import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 22 # pink
coil_A_2_pin = 23 # orange
coil_B_1_pin = 24 # blue
coil_B_2_pin = 25 # yellow

#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
# adjust if different

StepCount = 4
Seq4 = list(range(0, 4))
Seq4[0] = [1,0,1,0]
Seq4[1] = [0,1,1,0]
Seq4[2] = [0,1,0,1]
Seq4[3] = [1,0,0,1]


def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq4[j][0], Seq4[j][1], Seq4[j][2], Seq4[j][3])
            time.sleep(delay)

def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def stop():
    setStep(0,0,0,0)

if __name__ == '__main__':
    #print("Motors Stopped")
    stop()
    print("Motors Stopped")
