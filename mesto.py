import tkinter, random

sirka, vyska = 500, 300
canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()

farby = ('green', 'red', 'blue', 'purple', 'grey', 'yellow')
sipka = False  # este som nespustil obmedz
stare_poschodia = 0


def budova(x, poschodia, farba): # рисуем домик с этажами
    for i in range(poschodia): # для каждого этажа
        canvas.create_rectangle(x, vyska - 10 * i - 10, x - 10, vyska - 10 * i, fill=farba) # рисуем прямоугольник с цветом


def mesto(): # рисуем множество домиков
    print("mesto")
    for i in range(sirka // 10):  # sirka / 10 tolko krat + mesto ze zmensujeme x #
        poschodia = random.randint(1, 25) # задаем случайное количество этажей
        farba = random.choice(farby) # задаем случайный выбор цвета из списка
        budova(sirka - 10 * i, poschodia, farba) # вызываем фцию будова, чтобы нарисовать домик (ширина холста / i, этажи, цвет)


def posun():
    global stare_poschodia, sipka # используем глобальные переменные
    canvas.update() # перерисовываем холст
    canvas.move('all', -10, 0) # сдвигаем все на -10 пикс.

    farba = random.choice(farby) # случайно выбираем цвет

    if sipka: # если нажата стрелка
        print("🦆")
        poschodia = random.randint(1, stare_poschodia) # генерируем число от 1 до 0
        sipka = not sipka # сбрасываем состояние стрелки
    else:
        print("🐷")
        poschodia = random.randint(1, 25) # генерируем число от 1 до 25
        stare_poschodia = poschodia # присваиваем сгенерированное переменной stare poschodia

    budova(sirka, poschodia, farba) # рисуем дома

    canvas.after(5, posun) # снова вызываем фцию после 500
    print("end posun")


def obmedz(event):
    print("event")
    global sipka # используем глобальную
    sipka = not sipka  # neguj sipku # сбрасываем значение на противоположное


mesto() # рисуем домики
posun() # сдвигаем домики

canvas.bind_all('<Down>', obmedz) # << -- переместили привязку. иначе она не вызывается

canvas.mainloop()
