# Задача N 21 
# Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#          {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_of_dicts = [{"V": "S001"}, 
                 {"V": "S002"},
                 {"VI": "S001"}, 
                 {"VI": "S005"},
                 {"VII": "S005"},
                 {" V ": "S009"}, 
                 {" VIII": "S007"}]
uniq_el = set()
for i in list_of_dicts:
    element = list(i.values())[0]
    print(element)
    uniq_el.add(element)
print(uniq_el)    
