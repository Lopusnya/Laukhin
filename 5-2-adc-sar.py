import RPi.GPIO as GP

dac=[26,19,13,6,5,11,9,10]
comp=4
troyka=17
MaxVoltage=3.3
N=8

GP.setmode(GP.BCM)
GP.setup(dac,GP.OUT)
GP.setup(troyka,GP.OUT, initial=GP.HIGH)
GP.setup(comp,GP.IN)

def binary(a_bin):
    return[int(i) for i in bin(a_bin)[2:].zfill(8)]

def adc():

    signal_adc=[]
    VES=0
    for i in range(N-1,-1):

        ves=2**i+VES
        
        for j in range(8):
            GP.output(dac[j], a[j])

        if GP.input(comp)==0:
            signal_adc.append(0)
            continue
        else:
            signal_adc.append(1)
            VES+=ves

    return ves,signal_adc
    
try:

    while True:

        a,signal=adc()
        v = a * MaxVoltage / (2**N)
        
        for i in range(8):
            GP.output(dac[i], signal[i])
        
        if GP.input(comp)==0:
            print("Напряжение на компараторе = {:^2} -> {}, входное напряжение = {:.2}".format(a,signal,v))

finally:
    [GP.output(i, 0) for i in dac]
    GP.output(troyka, 0)
    GP.cleanup()