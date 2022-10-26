# Подключаем библиотеки
import numpy as np
import matplotlib.pyplot as plt 
from textwrap import wrap

# Открываем файл с периодом дискритизации и шагом квантования
with open("/home/b03-205/Desktop/Laukhin.Va.edu/settings.txt", "r") as settings:
    settings_array=[float(i) for i in settings.read().split("\n") ]

# Открываем файл с данными о замерах. И задаем шаг значениям.
data_array = np.loadtxt("/home/b03-205/Desktop/Laukhin.Va.edu/data.txt", dtype=int)
data_arrayvl=data_array * settings_array[0]

# Считаем время всего эксперимента. А также считаем время зарядки и разрядки
time=np.array([i*settings_array[1] for i in range(data_arrayvl.size)])
time_power = 0
time_lower =0
bufer = 0
for i in range(len(data_arrayvl)):
    if data_arrayvl[i] > bufer:
        time_power = time[i]
        bufer = data_arrayvl[i]
    else:
        time_lower = time[i]

# Задаем размер полотна и рисуем
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

# Задаем пределы
ax.axis([time.min(), time.max(), data_arrayvl.min(), data_arrayvl.max()+0.2])

# Шаг сетки
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))

# Подписи осей
ax.set_ylabel("Напряжение, мВ")
ax.set_xlabel("Время, с")

# Подпись Графика
ax.set_title("\n".join(wrap('Процесс зарядки и разрядки конденсатора в RC цепи' , 60)))

# Вывод времени зарядки и разрядки
ax.text(10, 1800, 'Время зарядки '+str(time_power)[:3])
ax.text(10, 1700, 'Время разрядки '+str(time_lower-time_power)[:3])

# Делем оси с шагом которым задавали выше
ax.minorticks_on()

# Присваиваем цвета главной и вторичной сетки
ax.grid(which='major', color = 'k', linewidth=2)
ax.grid(which='minor', color = 'gray', linestyle= ':')

# Непосредственно рисуем
ax.plot(time, data_arrayvl, 'o', ls='-', ms=4,markevery=10, color = 'r', label = 'V(t)')

# Легенду заносим
ax.legend()

# Сохраняем
fig.savefig("/home/b03-205/Desktop/Laukhin.Va.edu/graph.png")
fig.savefig("/home/b03-205/Desktop/Laukhin.Va.edu/graph.svg")

# Показываем что есть
plt.show()
