"""
Задача 2. Функция максимума
Что нужно сделать

Юра пишет различные полезные функции для Питона, чтобы остальным программистам стало проще работать.
Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. Функция для нахождения
максимума из двух чисел у него уже есть. Юра задумался: может быть, её можно как-то использовать для нахождения
максимума уже от трёх чисел?
Помогите написать Юре функцию, которая находит максимум из трёх чисел. Для этого используйте только функцию
нахождения максимума из двух чисел.
"""

def func_numb(a, b, c):
    numb_max = 0
    for n in a, b, c:
        if n > numb_max:
            numb_max = n
    return numb_max

numb_1 = float(input('Введите первое число: '))
numb_2 = float(input('Введите второе число: '))
numb_3 = float(input('Введите третье число: '))
max_numb = func_numb(numb_1, numb_2, numb_3)
print('Максимальное число: ', max_numb)
