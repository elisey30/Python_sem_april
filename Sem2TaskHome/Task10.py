# Задача №10

#  На столе лежат n монеток. Некоторые из них лежат вверх
#  решкой, а некоторые – гербом. Определите минимальное число
#  монеток, которые нужно перевернуть, чтобы все монетки были
#  повернуты вверх одной и той же стороной. Выведите минимальное
#  количество монет, которые нужно перевернуть.

from random import randint

count_many  = int(input('Введите кол-во монет: '))
oreal = 0
oresh = 0
for i in range(0, count_many, 1):
    num = randint(0,1)
    print(num)
    if num == 0:
        oresh += 1
    else:
     oreal += 1
if oresh > oreal:
    print(f'минимально количество монет, которые нужно перевернуть. {oreal}')  
else:
    print(f'минимально количество монет, которые нужно перевернуть. {oresh}')  

