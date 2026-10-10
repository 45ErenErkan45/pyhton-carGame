import turtle
import random

witdh,height=500,500
renkler=["red","green","blue","orange","yellow","black"]

def arabasayısı():
    while True:
        araba=0
        araba=input("araba sayısı seç: 2--6:")
        if araba.isdigit():
            araba=int(araba)
            if 2<=araba<=6:
               return araba
        else:
            print("2 ve 6 arasında olmak zorunda")


def yarıs(renklistesi):
    arabalistesi=araba_olusturma(renklistesi)
    while True:
        for araba in arabalistesi:
            hız=random.randrange(1,20)
            araba.forward(hız)

            x,y=araba.pos()
            if x>=witdh // 2 - 10:
                return renkler[arabalistesi.index(araba)]

def araba_olusturma(renklistesi):
    arabalistesi=[]
    mesafe=height//(len(renklistesi)+1)
    for i,renk in enumerate(renklistesi):
        araba=turtle.Turtle()
        araba.color(renk)
        araba.shape("triangle")
        araba.penup()
        araba.setpos(-witdh//2+20,height//2-mesafe*(i+1))
        araba.pendown()
        arabalistesi.append(araba)
    return arabalistesi

def turtle_ayarı():
    screen = turtle.Screen()
    screen.setup(witdh, height)
    screen.title("yarış oyunu")


arabalar = arabasayısı()
turtle_ayarı()

random.shuffle(renkler)
renklistesi = renkler[:arabalar]
kazanan=yarıs(renklistesi)
print(kazanan)

turtle.done()



