"""
Задача 2. Лестница
Что нужно сделать

Пользователь вводит число N. Напишите программу, которая выводит такую «лесенку» из чисел:
"""
numbers = int(input('Введите число: '))
for row in range(1, numbers + 1):
    for col in range(1, numbers + 1):
        if row >= col:
            print(row, end='\t')
        else:
            print(' ', end='\t')
    print()