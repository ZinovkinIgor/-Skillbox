"""
Задача 3. Убийца Steam
Что нужно сделать

Вы пишете программу-инсталлятор для компьютерной игры. Пока инсталлятор скачивает обновление, пользователю нужно
показать сколько процентов уже скачалось, чтобы он мог решить пойти заварить чаю, или подождать у экрана компьютера.
Обновления игры всегда занимают разное количество мегабайт, да и скорость интернет-соединения у игроков разная.
Напишите программу, принимающую на вход размер файла обновления в мегабайтах и скорость интернет соединения в
мегабайтах в секунду. Для каждой секунды программа рассчитывает и выводит на экран сколько процентов от всего
объема уже скачано, до тех пор пока не будет скачан весь объем. В конце программа должна показать сколько всего
секунд заняло скачивание обновления. Обеспечьте контроль ввода.

Пример:
Укажите размер файла для скачивания: 123
Какова скорость вашего соединения? 27
Прошло 1 сек. Скачано 27 из 123 Мб (22%)
Прошло 2 сек. Скачано 54 из 123 Мб (44%)
Прошло 3 сек. Скачано 81 из 123 Мб (66%)
Прошло 4 сек. Скачано 108 из 123 Мб (88%)
Прошло 5 сек. Скачано 123 из 123 Мб (100%)
"""
import math
file = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения? '))
uploaded, count = 0, 0
while file > uploaded:
    count += 1
    uploaded += speed
    if uploaded >= file:
        uploaded = file
    procent = math.ceil(uploaded / (file / 100))
    print('Прошло', count, 'сек. Скачано', uploaded, 'из', file, 'Мб(' + str(procent) + '%)')
