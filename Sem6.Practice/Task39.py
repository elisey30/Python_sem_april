# Задача № 39 
# Даны два массива чисел. Требуется вывести те уникальные 
# элементы первого массива (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. Элементы обоих массивов вводятся в две строки через пробел.
# Пример:
# 1 2 3 4 5 6
# 4 5 6 7 8 -> 1 2 3

first = [1, 2, 3, 4, 5, 6]
second = [4, 5, 6, 7, 8]
print ([i for i in first if i not in second])