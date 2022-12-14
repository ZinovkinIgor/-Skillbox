"""
Задача 1. Сумма чисел
Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке. Напишите программу,
которая выводит их сумму в выходной файл answer.txt.

Пример:
Содержимое файла numbers.txt:
1
2
3
4
10

Содержимое файла answer.txt
20

Задача 2. Всё в одном
Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город, и там у него случилась беда:
его диск пришлось отформатировать, а доступ в интернет отсутствует. Остался только телефон с мобильным интернетом.
Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом все решения и скрипты, которые у вас сейчас есть.
Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic в файл scripts.txt, разделяя
код строкой из 40 символов *.

Пример содержимого файла scripts.txt:
import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
****************************************
print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

print("Уравнение прямой, проходящей через эти точки:")
x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0:
    print("x = ", x1)
elif y_diff == 0:
    print("y = ", y1)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("y = ", k, " * x + ", b)
****************************************
"""
import os
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)
    summ = 0
    file = open('answer.txt', 'r')
    for numb in file:
        summ += int(numb)
    file.close()

    file_1 = open('numbers.txt', 'w')
    file_1.write(str(summ))
    file_1.close()

elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')


    def search_python_basic(adress):               # проходим по папкам и проверяем файлы если это .py то записываем в скрипт
        for name in os.listdir(adress):
            adr_1 = os.path.abspath(os.path.join(adress, name))
            if name.endswith('.py'):
                file = open(adr_1, 'r', encoding='utf-8')
                file_res = open('scripts.txt', 'a', encoding='utf-8')
                for name in file:
                    file_res.write(name)
                file.close()
                file_res.close()
                file_res = open('scripts.txt', 'a', encoding='utf-8')
                file_res.write('*' * 40)
                file_res.close()
            elif os.path.isdir(adr_1):
                search_python_basic(adr_1)



    adress = os.path.abspath(os.path.join('..', '..'))  # создаем адрес на курс
    search_python_basic(adress)


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

else:
    print('Выберите задачу заново.')