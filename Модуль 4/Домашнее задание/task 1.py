"""
Задача 1. Датчик погоды
Что нужно сделать

В квартире за окном стоит датчик погоды, который определяет, идёт дождь или нет.
Если пошёл дождь, датчик оповещает владельцев сообщением: «Пошёл дождь. Возьмите зонтик!»
Напишите программу, которая получает на вход число 0 или 1. Единица означает, что дождь идёт.
Если дождь идёт, то выводите на экран сообщение: «Пошёл дождь. Возьмите зонтик!»

Пример 1:
На улице идёт дождь? 1
Пошёл дождь. Возьмите зонтик!
Пример 2:
На улице идёт дождь? 0
"""

answer = int(input('На улице идёт дождь? '))
if answer == 1:
    print('Пошёл дождь. Возьмите зонтик.')
else:
    print('')