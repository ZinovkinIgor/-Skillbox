"""
Задача 1. Курс от Skillbox-2
Напишите программу для примера, разобранного в уроке.
Пользователь покупает курс стоимостью 75 000 рублей.
Если денег на счету достаточно, нужно списать деньги и вывести сообщение: «Курс успешно приобретён»,
 — а иначе вывести: «Не хватает денег на счёте».
Не забудьте пожелать «Хорошего дня!» в любом случае. Мы же вежливые продавцы.

Пример:
Сколько денег на счету? 5000
Не хватает денег на счету.
Хорошего дня!

Задача 2. Разминка для мозгов
Напишите программу, которая проверяет то, как вы умеете складывать два числа в уме.
Программа получает на вход два числа и предполагаемую сумму и должна выводить два разных сообщения —
на верный и неверный ответ пользователя. В последнем случае надо показывать правильный результат.

Пример:
Введите первое число: 3
Введите второе число: 10
Сумма этих чисел: 13
Ответ верный!

Пример 2:
Введите первое число: 3
Введите второе число: 10
Сумма этих чисел: 14
Ответ неверный!

Задача 3. Угадай число 2
На удивление, отец и сын частенько стали играть в игру «Угадай число»,
и поэтому папа захотел немного усовершенствовать свою программу, чтобы на экран всегда выводилось нужное сообщение.
Напишите программу, которая запрашивает число у пользователя, сравнивает его с
другим числом и выводит соответствующее сообщение: «Угадал», — если они равны,  и:
«Не угадал», — если не равны. В конце выводите фразу: «Конец игры».

Пример 1:
Какое число я загадал? 5
Угадал!
Конец игры

Пример 2:
Какое число я загадал? 6
Не угадал!
Конец игры

Попробуйте решить задачу сначала с помощью одного знака сравнения (==), а затем с помощью другого (!=).
"""

# Задача 1
print('=' * 40)
print('Задача 1')
price = 75000
bank = int(input('Введите сумму ваших денег: '))
if bank >= price:
    print('Поздравляю вы приобрели курс.')
else:
    print('Мало денег.')
print('Хорошего дня!')

# Задача 2
print('=' * 40)
print('Задача 2')
numb1 = int(input('Введите первое число: '))
numb2 = int(input('Введите второе число: '))
answer = int(input('Введите ответ: '))
if numb1 + numb2 == answer:
    print('Ответ верный!')
else:
    print('Ответ неверный!')

# Задача 3
print('=' * 40)
print('Задача 3')
father_number = 8
numbers = int(input('Введите число: '))
if father_number == numbers:
    print('Угадал!')
else:
    print('Не угадал!')
print('Конец игры.')