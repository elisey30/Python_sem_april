#  Задача No15. 

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, 
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, 
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает 
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, 
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 Output: 1 9

number = int(input('Введите кол-во арбузов: '))
if number > 30000 or number < 1: # проверяем что бы число было от 1 до 100
  raise ' период должен быть от 1 до 30000'
min_weight = 30001
max_weight = 1
for i in range(0, number, 1):
    weight = int (input('вес: '))
    #print(weight)
    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight
print(f' арбуз для себя {max_weight}')  
print(f' арбуз для тещи {min_weight}')      

