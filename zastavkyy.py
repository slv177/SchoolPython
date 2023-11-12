import tkinter
canvas = tkinter.Canvas(width = 400,height = 100, bg = 'black')
canvas.pack()

f = open('zastavky1 1.txt','r')
zastavky = f.read().split('\n') #zoznam
f.close()

text = canvas.create_text(400,50,text = '',font = 'Courier 20',
                              fill = 'red')
start = 0
pp = False

def vymaz(event):
    global start,pp
    print('ahoj')
    zastavky.pop(0)
    start += 1
    pp = True

canvas.bind_all('<space>',vymaz)

def slucka():
    global start,pp
    zastavka = 0
    while len(zastavky)>zastavka:
        
        if pp:
            zastavka -=1
            pp = False
            
        canvas.coords(text,400+len(zastavky[zastavka])*2/3*20,50)
        canvas.itemconfig(text,text = zastavky[zastavka])
        
        for i in range(0,400):
            canvas.move(text, -(400+(len(zastavky[zastavka])*4/3*20))/400,0)
            canvas.after(1)
            canvas.update()
            
        zastavka += 1
        
    canvas.after(1,slucka)


slucka()
