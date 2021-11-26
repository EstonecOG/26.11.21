from random import *
inimesed = ["A", "B", "C", "D"]
palgad = [3000, 2000, 1000, 2000]
def sisesta_andmed(i, p):
    """Добавление юзера в список, а также зарплата
    """
    N = 1
    for n in range(N):
        inimene = input("Введите имя: ")
        i.append(inimene)
        palk=int(input("Введите зарплату: "))
        p.append(palk)
    return i,p
def andmed_ekranile(i, p):
    """Показать список людей и зарплат
    """
    N=len(i)
    for n in range(N):
        print(f"{i[n]} - {p[n]}")
def kustutamine(i, p):
    """Удаляет имя и зарплату человека из списка
    """
    nimi=input("Введите имя человека, которого нужно удалить: ")
    n=i.count(nimi)
    abi_list=[]
    if n > 0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e))
                print(f"{t}.{i[e]} - {p[e]}")
        j=int(input("Порядковый номер человека: "))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p
def maksimum(i, p):
    """Выводит макимальную зарплату юзера из списка на экран
    """
    max_palk = palgad[0] 
    kellel = inimesed[0]
    for p in palgad:
        if p > max_palk:
            max_palk = p
            i = palgad.index(max_palk)
            kellel = inimesed[i]
    print(f"Максимальную зарплату - {max_palk} получает - {kellel}")
def minimum(i, p):
    """Выводит минимальную зарплату юзера из списка на экран
    """
    min_palk = palgad[0]
    kellel = inimesed[0]
    for p in palgad:
        if p < min_palk:
            min_palk = p
            i = palgad.index(min_palk)
            kellel = inimesed[i]
    print(f"Минимальную зарплату - {min_palk} получает - {kellel}.")