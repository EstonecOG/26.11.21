from random import *
from module1 import *
import keyboard
inimesed = ["A", "B", "C", "D"]
palgad = [3000, 2000, 1000, 2000]

while 1:
    valik=input("e -Показать данные \nk - Удаление\nmax - Максимальная зарплата\nmin - Минимальня зарплата\ns - Добавить юзера")
    if valik.lower() == "e":
        andmed_ekranile(inimesed,palgad)
    elif valik.lower() == "k":
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower() == "max":
        maksimum(inimesed, palgad)
    elif valik.lower() == "min":
        minimum(inimesed, palgad)
    elif valik.lower() == "s":
        sisesta_andmed(inimesed, palgad)
    else:
        break
