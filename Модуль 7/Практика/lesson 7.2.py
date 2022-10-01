"""
Задание 1. Дом для семьи
Максим написал программу, которая должна определять, подходит ли земельный участок для его семьи или нет.
Живут они втроем, вот и условие будет таким же: если количество квадратных метров делится на 3, то участок подходит.

For in meters 100,90,95,87,102:
 if meters % 3 == 1:
   print(meters, 'Подходит')
 else:
   print(meters, 'Не подходит')
Скопируйте программу в редактор и исправьте её. Убедитесь, что она работает правильно и решает задачу Максима.

Задание 2. Таблица степеней
Аркадию для выступления с докладом нужно выучить таблицу степеней для определённых чисел. Правда,
память у него работает довольно необычно, и ему проще учить их в нужном ему порядке.
Напишите программу, которая выводит вторую, третью и четвёртую степень для каждого числа в отдельной строке
(первая строка - степени для числа 3, вторая строчка - степени для числа 7 и т.д.). Числа: 3,7,5,6,4.

Результат:
9 27 81
49 343 2401
25 125 625
36 216 1296
16 64 256

Задача 3. Лотерея 2
Напишите программу для немного усложнённой версии задачи про выигрышные билеты. Есть заранее известные номера билетов:
345, 19, 87, 1020 и 421 (можете брать свои номера, не стесняйтесь). Теперь, билет считается выигрышным, если номер билета
- трёхзначное число и оно делится на 5. Выведете в консоль сообщение для каждого выигрышного билета и количество победителей.
"""
# Задача 1
print('=' * 40)
print('Задача 1')
for meters in 100, 90, 95, 87, 102:
    if meters % 3 == 0:
        print(meters, 'Подходит')
    else:
        print(meters, 'Не подходит')
# Задача 2
print('=' * 40)
print('Задача 2')
for num in 3, 7, 5, 6, 4:
    print(num ** 2, num ** 3, num ** 4)

# Задача 3
print('=' * 40)
print('Задача 3')
count = 0
for num in 345, 19, 87, 1020, 421:
    if num % 5 == 0 and num >= 100 and num < 1000:
        print(num, 'Билет выиграл!')
        count += 1
print('Всего выиграло билетов:', count)