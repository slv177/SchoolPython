import tkinter

canvas = tkinter.Canvas(width=400, height=100, bg='black') # формируем холст
canvas.pack() # отрисовка холста

f = open('zastavky1 1.txt', 'r') # открываем файл для чтения
zastavky = f.read().split('\n')  # zoznam формируем список остановок
f.close() # закрываем файл

text = canvas.create_text(400, 50, text='', font='Courier 20', fill='red') # создаем текст с координатами с свойствами
start = 0 # создаем указатель на первый элемент списка
pp = False


def vymaz(event): # определяем фцию для удаления следующего элемента
    global start, pp # нам надо работать со списком, который находится вне функции и менять указатель, который
    # сформирован вне фции и сохранять его значение
    print("def vymaz: ", zastavky.pop(0)) # выбрасываем первый элемент списка остановок
    start += 1 # переводим указатель на след элт
    pp = True


canvas.bind_all('<space>', vymaz) # привязываем кнопку пробела к запуску фции vymaz


def slucka():
    print("def slucka")
    global start, pp # используем переменные которые определены вне фции
    zastavka = 0 # создаем указатель на первый элемент в списке
    while len(zastavky) > zastavka: # проходим по каждому элементу в списке

        if pp: # если pp, то
            print("if pp")
            zastavka -= 1 # уменьшаем указатель на единицу
            print("new zastavka: ", zastavky[zastavka])
            pp = False # и pp в этой итерации не запускаем

        canvas.coords(text, 400 + len(zastavky[zastavka]) * 2 / 3 * 20, 50) # задаем координаты текста в виде списка
        canvas.itemconfig(text, text=zastavky[zastavka])

        for i in range(0, 400): # сдвигаем текст
            canvas.move(text, -(400 + (len(zastavky[zastavka]) * 4 / 3 * 20)) / 400, 0) # от 400 до 0
            canvas.after(1) # после 1  миллисекунды
            canvas.update() # перерисовываем холст

        zastavka += 1 # переходим к следующей остановке

    # canvas.after(1, slucka) # после 1 мс запускаем фцию slucka снова. зачем?


slucka() # запускаем главный цикл
