"""
Задача 9. В обратном порядке
Что нужно сделать

Реализуйте программу, которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
Однако можно использовать сколько угодно переменных. Пример ввода: 1234. Пример вывода: 4321.
"""
numbers = int(input('Введите число: '))
a = numbers // 1000
b = (numbers // 100) % 10
c = (numbers // 10) % 10
d = numbers % 10
print(str(d) + str(c) + str(b) + str(a))