"""
Задача 5. Песни
Что нужно сделать
Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти песен группы Depeche Mode.
Каждая песня состоит из названия и продолжительности с точностью до долей минут:
violator_songs = [
    ['World in My Eyes', 4,86],
    ['Sweetest Perfection', 4,43],
    ['Personal Jesus', 4,56],
    ['Halo', 4,9],
    ['Waiting for the Night', 6,07],
    ['Enjoy the Silence', 4,20],
    ['Policy of Truth', 4,76],
    ['Blue Dress', 4,29],
    ['Clean', 5,83]
]

Из этого списка Ваня хочет выбрать N песен и закинуть их в особый плейлист с другими треками. И при этом ему важно,
сколько времени в сумме эти N песен будут звучать.
Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен,
а на экран выводит общее время их звучания.

Пример:
Сколько песен выбрать? 3
Название 1-й песни: Halo
Название 2-й песни: Enjoy the Silence
Название 3-й песни: Clean

Общее время звучания песен: 14,93 минуты
"""

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
new_music = []
playlist = int(input('Сколько песен выбрать? '))
for num in range(1, playlist + 1):
    print('Название', num, '- й песни: ', end='')
    track = input()
    for sond in violator_songs:
        if track in sond and track not in new_music:
            new_music.append(sond)
            break
sum_music = 0
for i_time in range(len(new_music)):
    sum_music += new_music[i_time][1]
print('Общее время звучания песен:', sum_music, 'минуты')

