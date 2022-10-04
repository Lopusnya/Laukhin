import RPi.GPIO as GPIO
import time

def binary(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
[GPIO.setup(i, GPIO.OUT) for i in dac]
t = float(input())
try:
    while 1:
        

        for ch in range(0, 255, +1):
            a = binary(int(ch))
            [GPIO.output(dac[i], a[i]) for i in range(8)]
            time.sleep(t/512)

        for ch in range(255, 0, -1):
            a = binary(int(ch))
            [GPIO.output(dac[i], a[i]) for i in range(8)]
            time.sleep(t/512)
        
finally:
    [GPIO.output(i, 0) for i in dac]
    GPIO.cleanup()
