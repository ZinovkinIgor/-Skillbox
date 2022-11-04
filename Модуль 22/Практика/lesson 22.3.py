"""
Задача 1. Результаты
Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей.
Файл первой группы (group_1.txt) находится в папке task, файл второй группы (group_2.txt) — в папке Additional_info.

Содержимое файла group_1.txt
Бобровский Игорь 10
Дронов Александр 20
Жуков Виктор 30

Содержимое файла group_2.txt
Павленко Геннадий 20
Щербаков Владимир 35
Marley Bob 15

На экран нужно было вывести сумму очков первой группы, затем разность очков опять же первой группы и
напоследок — произведение очков уже второй группы.
Программист оказался не очень опытным, писал код наобум и даже не стал его проверять. И оказалось,
этот код просто не работает. Вот что он написал:

file = open('E:\task\group_1.txt', 'read')
summa = 0
for i_line in file:
    info = i_line.split()
    summa += info[2]
file = open('E:\task\group_1.txt', 'read')
diff = 0
for i_line in file:
    info = i_line.split()
    diff -= info[2]
file_2 = open('E:\task\group_2.txt', 'read')
compose = 0
for i_line in file:
    info = i_line.split()
    compose *= info[2]
print(summa)
print(diff)
print(compose)

Исправьте код для решения поставленной задачи. Для проверки результата создайте необходимые папки
(task, Additional_info, Dont touch me) на своём диске в соответствии с картинкой и также добавьте
файлы group_1.txt и group_2.txt.

Задача 2. Поиск файла 2
Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту.
Таким образом, с ними можно работать точно так же, как и с обычными текстовыми файлами.
Используя функцию поиска файла из предыдущего урока, реализуйте программу, которая находит внутри
указанного пути все файлы с искомым названием и выводит на экран текст одного из них (выбор можно сгенерировать случайно).
Подсказка: можно использовать, например, список для сохранения найденного пути.
"""
import os

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    def processing(path, name):
        summ_1, summ_2, flag = 0, 0, False
        for i_name in os.listdir(path):
            adr = os.path.abspath(os.path.join(os.path.sep, path, i_name))
            if os.path.isdir(adr):
                processing(adr, name)
            elif i_name == name:
                print('\nЭто файл: {}'.format(i_name))
                file = open(adr, 'r', encoding='utf-8')
                res_file = file.read()
                for res in res_file.split('\n'):
                    new_list = [i_res for i_res in res.split()]
                    summ_1 += int(new_list[2])
                    summ_2 -= int(new_list[2])
                print(summ_1)
                print(summ_2)


    name_list = ['group_1.txt', 'group_2.txt']
    path = os.path.abspath(os.path.join('..'))

    result = processing(path, name_list[0])
    result_1 = processing(path, name_list[1])


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    def search_file(adress, files):
        for name in os.listdir(adress):
            adr_1 = os.path.abspath(os.path.join(os.path.sep, adress, name))
            if name.startswith(files):
                print(os.path.join(adress, name))
                print(adr_1)
            elif os.path.isdir(adr_1):
                search_file(adr_1, files)

    adress = os.path.abspath(os.path.join(os.path.sep, 'Users', 'User', 'OneDrive'))
    print(adress)
    files = input('Введите название файла для поиска: ')
    search_file(adress, files)


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

    def search_file(adress, files):

        for name in os.listdir(adress):
            adr_1 = os.path.abspath(os.path.join(os.path.sep, adress, name))
            if name.endswith(files):
                print(os.path.join(adress, name))
                print(adr_1)
                file = open('adress.txt', 'a', encoding='utf-8')
                file.write('{}\n'.format(adr_1))
                file.close()
            elif os.path.isdir(adr_1):
                search_file(adr_1, files)


    adress = os.path.abspath(os.path.join(os.path.sep, 'Users', 'User', 'OneDrive'))
    print(adress)
    files = input('Какое расширение ищем: ')
    search_file(adress, files)


else:
    print('Выберите задачу заново.')