"""
Задача 8. «Режем» число на части
Что нужно сделать

Реализуйте программу, которая получает на вход четырёхзначное число и выводит на экран каждую его цифру отдельно
(в одну строчку либо каждую цифру в новой строчке). Само число при этом изменять нельзя, то есть нужно обойтись
без переприсваивания. Однако можно использовать сколько угодно переменных.
"""
numbers = int(input('Введите число: '))
num1 = numbers % 10
num2 = (numbers // 10) % 10
num3 = (numbers // 100) % 10
num4 = numbers // 1000
print(num4, num3, num2, num1)