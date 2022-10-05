import RPi.GPIO as GP
import time

dac=[26,19,13,6,5,11,9,10]
comp=4
troyka=17
MaxVoltage=3.3
N=8

GP.setmode(GP.BCM)
GP.setup(dac,GP.OUT)
GP.setup(troyka,GP.OUT, initial=GP.HIGH)
GP.setup(comp,GP.IN)

def binary(a_ch):
    return[int(i) for i in bin(a_ch)[2:].zfill(8)]

def adc():
    for i in range(2**N):
        return i
    
try:

    while True:

        ch=adc()
        v = ch * MaxVoltage / (2**N)
        a = binary(ch)

        for i in range(8):
            GP.output(dac[i], a[i])

        time.sleep(0.005)
        
        if GP.input(comp)==0:
            print("Напряжение на компараторе = {:^2} -> {}, входное напряжение = {:.2}".format(ch,a,v))

finally:
    [GP.output(i, 0) for i in dac]
    GP.output(troyka, 0)
    GP.cleanup()