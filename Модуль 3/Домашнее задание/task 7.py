"""
Задача 7. Поездка по кругу
Что нужно сделать
Вася решил потренироваться перед марафоном и покататься вокруг Москвы на скорость.
Длина дороги — 115 километров. Вася стартует с нулевого километра и едет со скоростью v километров в час.
На какой отметке он остановится через t часов?
Реализуйте программу, которая спрашивает у пользователя v и t и выводит целое число от 0 до 114 — номер километра,
на котором остановится Вася. Учтите, что он может прокатиться больше одного круга.

Пример
Введите скорость (км/ч): 100
Введите время (ч): 2
Ответ: 85 км
Пройденное расстояние составит 200 км, значит Вася будет на отметке 85 км.
"""

lenght = 115
speed = int(input('Введите скорость (км/ч): '))
time = int(input('Введите время (ч): '))
res1 = speed * time
res2 = (speed * time) % lenght
print('Ответ:', res2)
print('Пройденное расстояние составит', res1, 'км, значит Вася будет на отметке', res2, 'км.')