"""
Задача 1. Словарь квадратов чисел
На вход программе поступает целое число num. Напишите программу создания словаря, который включает в себя ключи от 1 до num,
а значениями соответствующего ключа будет значение ключа в квадрате.

Пример:
Введите целое число: 5
Результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

Задача 2. Студент
Пользователь вводит фамилию, имя студента, город проживания, вуз, в котором он учится, и все его оценки.
Всё вводится в одну строку через пробел. Напишите программу, которая по этой информации составит словарь и выведет его на экран.

Пример:
Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): Илья Иванов Москва МГУ 5 4 4 4 5

Результат:
Имя - Илья
Фамилия - Иванов
Город - Москва
Место учёбы - МГУ
Оценки - [5, 4, 4, 4, 5]

Задача 3. Контакты
Энтузиаст Степан, купив новый телефон, решил написать для него свою собственную операционную систему.
И, конечно же, первое, что он захотел в ней реализовать, — это телефонная книга.
Напишите программу, которая запрашивает у пользователя имя контакта и номер телефона, добавляет их в словарь и
выводит на экран текущий словарь контактов. Запрос на добавление идёт бесконечно (но можно задать своё условие для
завершения программы). Обеспечьте контроль ввода: если это имя уже есть в словаре, то выведите соответствующее сообщение.

Пример:
Текущие контакты на телефоне:
<Пусто>

Введите имя: Иван
Введите номер телефона: 100200300
Текущие контакты на телефоне:
Иван  100200300

Введите имя: Лена
Введите номер телефона: 8005555522
Текущие контакты на телефоне:
Иван  100200300
Лена  8005555522

Введите имя: Иван
Ошибка: такое имя уже существует.
"""

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)
    numbers = int(input('Введите целое число: '))
    result_dict = dict()
    for i_num in range(1, numbers + 1):
        result_dict[i_num] = i_num ** 2
    print(result_dict)

elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    student_dict = dict()
    student = input('Введите информацию о студенте через пробел '
                    '\n(имя, фамилия, город, место учёбы, оценки): ')
    student = student.split()
    student_dict['Имя'] = student[0]
    student_dict['Фамилия'] = student[1]
    student_dict['Город'] = student[2]
    student_dict['Место учебы'] = student[3]
    student_dict['Оценки'] = []
    for num in student[4:]:
        student_dict['Оценки'].append(int(num))
    print(student_dict)
    for i_num in student_dict:
        print(i_num, '-', student_dict[i_num])

elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')
    phone_contacts = dict()
    while True:
        print('Текущие контакты на телефоне:')
        for name in phone_contacts:
            print(name, phone_contacts[name])
        human = input('\nВведите имя: ')
        number = int(input('Введите номер телефона: '))
        if human == 'end':
            break
        if human not in phone_contacts:
            phone_contacts[human] = number
        else:
            print('\nОшибка: такое имя уже существует.\n')




else:
    print('Выберите задачу заново.')