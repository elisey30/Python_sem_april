# Задача № 4 
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*

#6 -> 1  4  1
#24 -> 4  16  4
#    60 -> 10  40  10
#    7 -> "нельзя определить"

summa = int(input("введите число:  ")) # кладем в summa введенное пользователем число 
Katy = int((summa / 3) * 2) # Вводим переменную Katy, вычисляем кол-во сделаных ей журавликов
Pety = int((Katy / 2) / 2) # Вводим переменную Pety, вычисляем кол-во сделанных им журавликов
Sergey = int(Pety) # Вводим переменную Sergey, т к они сделали одинаковое кол-во с Pety кладем туда его кол-во
if summa == Pety + Sergey + Katy: # если сумма введенная пользователем равна сумме наших вычислений
    print(Sergey, Katy, Pety) # печатаем кол-во сделанных ими журавликов
else:
    print(" нельзя определить: ") # если нет , выводим нельзя определить 