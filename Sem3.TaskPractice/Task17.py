# Задача N 17
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
 
nums = [1, 1, 2, 0, -1, 3, 4, 4]
print(nums)

result = []
for i in set(nums):
    if nums.count(i) == 1:
        result.append(i)
print(result)