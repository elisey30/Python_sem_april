# Задача № 35
# Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

def prostoe(k:int) -> str:
    """Принимает число выдает простое ли оно"""
    if k > 1:
        for i in range(2,int(k/2)+1):
            if (k % i) == 0:
                return "это не простое число"
    return "Это простое число"  
k = int(input("Введите число: "))
print(prostoe(k))      