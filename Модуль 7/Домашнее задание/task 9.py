"""
Задача 9. ...Теперь можно посчитать и свою
Что нужно сделать

Пока бухгалтер считала среднюю зарплату сотрудников, ей стало интересно, а не зря ли она работает столько времени
на одном месте? Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
Пользователь вводит десять чисел. Напишите программу, которая проверяет, упорядочены ли они по возрастанию.
"""
old_salary = 0
flag = False
for month in range(1, 11):
    new_salary = int(input('Введите вашу зарплату: '))
    if new_salary >= old_salary:
        print('Зарплата растет или стоит на месте:')
    else:
        print('Зарплата падает.')
        flag = True
    old_salary = new_salary
if flag:
    print('Зарплата нестабильная.')
else:
    print('Зарплата растет.')

