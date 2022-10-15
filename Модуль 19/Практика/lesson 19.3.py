"""
Задача 1. Член семьи
Дана структура, которая содержит описание одного из членов семьи (имя, фамилия, хобби, сколько лет и дети):
family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

Напишите программу, которая реализует такую структуру: имя, фамилия, хобби, кол-во лет и дети. Затем, с
помощью метода get и установки значения по умолчанию, проверьте есть ли ребёнок с именем Bob. Затем в
отдельную переменную получите фамилию этого ребёнка и выведите её на экран. Если у него нет фамилии,
то получите значение ‘Nosurname’.

Задача 2. Игроки
Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет, а также его текущий статус,
в котором указано, отдыхает он, тренируется или путешествует:
players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

Напишите программу, которая выводит на экран вот такие данные в разных строчках:
Все члены команды из команды А, которые отдыхают.
Все члены команды из группы B, которые тренируются.
Все члены команды из команды C, которые путешествуют.
"""
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)
    print('Задача 1')

    family_member = dict()
    human = input('Введите через пробел имя, фамилию, кол-во лет: ').split()
    hobbi = input('Введите хобби через пробел: ').split()
    scor_children = int(input('Введите сколько детей: '))

    family_member['name'] = human[0]
    family_member['surname'] = human[1]
    family_member['hobbies'] = []
    family_member['age'] = human[2]
    family_member['children'] = {}
    for hob in hobbi:
        family_member['hobbies'].append(hob)
    for child in range(scor_children):
        name = input('Введите имя и возраст ребенка через пробел: ').split()
        family_member['children'][name[0]] = name[1]
    search = input('Введите имя ребенка для поиска: ')
    if family_member.get('children').get(search):
        print(family_member['surname'], search)
    else:
        print('Такого ребенка нет.')


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')


    players_dict = {
        1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
        2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
        3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
        4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
        5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
        6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
        7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
        8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
    }

    result_2 = [
        i_num['name']
        for i_num in players_dict.values()
        if i_num['team'] == 'A' and i_num['status'] == 'Rest'
    ]
    print(result_2)

    result_2 = [
        i_num['name']
        for i_num in players_dict.values()
        if i_num['team'] == 'B' and i_num['status'] == 'Training'
    ]
    print(result_2)

    result_3 = [
        i_num['name']
        for i_num in players_dict.values()
        if i_num['team'] == 'C' and i_num['status'] == 'Travel'
    ]
    print(result_3)


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

else:
    print('Выберите задачу заново.')