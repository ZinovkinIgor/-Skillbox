"""
Задача 1. Меню ресторана
Что нужно сделать
Один ресторан заказал вам написать приложение, которое в один клик отображало бы пользователю доступное меню в
удобном виде. Для этого ресторан любезно предоставил свой сайт, откуда можно получить актуальную информацию о
меню в виде идущих подряд названий.

Напишите программу, которая выводит это меню на экран. На вход подаётся строка из названий блюд, разделённых
символом «;», а на выходе эти названия перечисляются через запятую и пробел.
"""

menu = input('Введите названия блюд через ";" : ').split('; ')
new_menu = ', '.join(menu)
print(new_menu)