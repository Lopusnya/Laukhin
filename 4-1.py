import RPi.GPIO as GPIO


def binary(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
[GPIO.setup(i, GPIO.OUT) for i in dac]

try:
    while True:
        
         ch = input()
         if ch == 'q':
             break
         if ch.isdigit() and 0 <= int(ch) <= 255:
             v = int(ch) * 3.3 / 256
             print(v, "B")
             a = binary(int(ch))
             for i in range(8):
              GPIO.output(dac[i], a[i]) 
              
        
         else:
          print("Введите число от 0 до 255: ")
         
        
finally:
    [GPIO.output(i, 0) for i in dac]
    GPIO.cleanup()
