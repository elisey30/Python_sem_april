# Задача № 14 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

num = int(input('введите число N: '))
degree = 0
while 2 ** degree < num:
    print(2 ** degree)
    degree += 1