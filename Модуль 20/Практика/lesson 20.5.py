"""
Задача 1. Паспортные данные
В базе данных поликлиники хранятся паспортные данные людей. Хранение реализовано с помощью словаря, состоящего
из пар «Серия и номер паспорта — фамилия и имя». Серия и номер — составной ключ, а фамилия и имя — составное значение.

data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

Реализуйте функцию, которая по номеру и серии паспорта выдаёт имя и фамилию человека.

Задача 2. Контакты 2
Мы уже реализовывали телефонную книгу для Степана, однако её проблема была в том, что туда нельзя было добавить
людей с одинаковыми именами. Надо это исправить.
Напишите программу, которая запрашивает у пользователя имя контакта, фамилию и номер телефона, добавляет их в словарь
и выводит на экран текущий словарь контактов. Словарь состоит из пар «Ф. И. — телефон», где Ф. И. — это составной ключ.
Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы). Обеспечьте контроль ввода:
если этот человек уже есть в словаре, то выведите соответствующее сообщение.
"""

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    data = {
        (5000, 123456): ('Иванов', 'Василий'),
        (6000, 111111): ('Иванов', 'Петр'),
        (7000, 222222): ('Медведев', 'Алексей'),
        (8000, 333333): ('Алексеев', 'Георгий'),
        (9000, 444444): ('Георгиева', 'Мария')
    }

    numbers = input('Введите серию и номер паспорта: ').split()
    numb = tuple(numbers)
    for i_key, i_value in data.items():
        if int(numb[0]) == i_key[0]:
            if int(numb[1]) == i_key[1]:
                print(i_value)


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    telephone = dict()

    while True:
        print(telephone)
        contact = input('Введите Фамилию, Имя, номер телефона: ').split()
        if contact[0] in telephone:
            if contact[1] in telephone:
                print('Контакт уже существует.')
            else:
                telephone[(contact[0], contact[1])] = contact[2]
        else:
            telephone[(contact[0], contact[1])] = contact[2]



elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

else:
    print('Выберите задачу заново.')
