#  Задача № 9. 
# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120

number = int(input('Введите число n: ')) 
count = 1
summa = 1
while count <= number:
    summa = summa * count
    count += 1
print(summa)
