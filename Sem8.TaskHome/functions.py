def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('sem_8_practice/book.txt','r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('sem_8_practice/book.txt','a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('sem_8_practice/book.txt','r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)    


def search(book: list[str], info: str) -> list[str] or str:
    """Находит в списке записи по определенному критерию поиска"""
    with open('sem_8_practice/book.txt', 'r', encoding='utf-8') as book:
        result = [contact for contact in book if info in contact]
    if not result:
        return 'Совпадений не найдено'
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('----------------')
        print('\n'.join(result))
        new_info = input(' Введите данные для уточнения: ')
        return search(result, new_info)
    
def chenge() -> None:
    """Изменение/удаление данных в справочнике."""
    with open('sem_8_practice/book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print('\n'.join(data))
    data_to_edit = input('Введите данные для поиска: ')
    data_to_edit = search(data, data_to_edit)
    print(f'Выбранный контак: {data_to_edit}')
    mode = input('удалить или изменить? 1 - удалить, 2 - изменить  ')
    if mode == '1':
        data.remove(data_to_edit)
    elif mode == '2':
        data[data.index(data_to_edit)] = enter_contact()

    with open('sem_8_practice/book.txt','w', encoding='utf-8') as file:
        file.write('\n'.join(data))

def enter_contact() -> str:
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    return f'{fio} | {phone}'









# data = 'фио | номер телефона\n\
# фио1 | номер телефона1\n\
# Исаев Владислав Иванович | +814881481848\n\
# Иванов Иван Иванович | +79874532'
# print(data)
# contact_to_find = input('Введите, что хотите найти: ')
# print(search(data, contact_to_find))
