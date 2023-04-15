# Задача N 23
# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов массива, больших предыдущего
# (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

num = [0, -1, 5, 2, 3]
print(num)
count = 0
for i in range(1,len(num)):
    if num[i - 1] > num[i]:
        count += 1
print(count)