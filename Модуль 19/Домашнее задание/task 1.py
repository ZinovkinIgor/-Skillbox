"""
Задача 1. Песни 2
Что нужно сделать
Мы продолжаем писать приложение для удобного прослушивания музыки, но теперь наши песни хранятся в виде словаря,
а не вложенных списков. Каждая песня состоит из названия и продолжительности с точностью до долей минут.

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

Напишите программу, которая запрашивает у пользователя количество песен из списка и названия этих песен,
а на экран выводит общее время их звучания.

Пример:
Сколько песен выбрать? 3
Название первой песни: Halo
Название второй песни: Enjoy the Silence
Название третьей песни: Clean
Общее время звучания песен: 14,93 минуты
"""

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
play_list = set()
scor = int(input('Сколько песен выбрать? '))
for num in range(1, scor + 1):
    print('Название {} песни: '.format(num), end='')
    music = input()
    play_list.add(music)
time_play_list = sum([float(violator_songs[trak]) for trak in violator_songs if trak in play_list])

print('Общее время звучания песен: {} минуты'.format(round(time_play_list, 2)))
