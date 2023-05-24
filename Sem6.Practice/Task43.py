# Задача № 43
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на одной строке через пробел.
# 1 2 1 3 4 5 3 4 -> 3
# 1 2 1 3 4 3 1 -> 2


def metod (some_list: list)->int:
    count = 0
    for i in set(some_list):
        num = some_list.count(i)
        if num > 1:
            count += num // 2
    return round(count, 0)
first = [1, 2, 1, 3, 4, 5, 3, 4]
second = [1, 2, 1, 3, 4, 3, 1]
print(metod(first))    
print(metod(second)) 