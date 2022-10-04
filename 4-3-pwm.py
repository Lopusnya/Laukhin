import RPi.GPIO as GP

#Задай номер пина который хочешь настроить на ШИМ
pin=24
GP.setmode(GP.BCM)
GP.setup(pin,GP.OUT)
try:
    while TRUE:
        print("Для остановки программы введите: stop")
        dc=input("Введи коэфициент заполнения: ")
        if dc == "stop":
            break
        if dc.isdigit():
            v = 100/int(dc) * 3.3
            print(v, "B")
            a=GP.PWM(pin,1000)
            a.start(dc)
            input("Нажми enter чтобы остановить ШИМ")
            a.stop()
        else:
            print("Вводите число от 0 до 100, а не символы!")
    
finally:
    GP.output(pin,0)
    GP.cleanup()

