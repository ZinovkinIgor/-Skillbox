"""
Задача 10. Игра «Компьютер угадывает число»
Что нужно сделать

Поменяйте мальчика и компьютер из прошлой задачи местами. Теперь мальчик загадывает число между 1 и 100 (включительно).
Компьютер может спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?», где N — число,
которое хочет проверить компьютер. Мальчик отвечает одним из трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
Напишите программу, которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

Подсказка:
Используйте бинарный поиск, а не конкатенацию.
"""
score, num_min, num_max = 0, 0, 100

numbers = int(input('Мальчик вводит число: '))
while True:
    score += 1
    num = num_min + ((num_max - num_min) // 2)
    print('Попытка', score, 'Ваше число', num)
    result = int(input('Выбери ответ: (1 — равно, 2 — больше, 3 — меньше) '))
    if result == 1:
        break
    elif result == 2:
        num_min = num
    elif result == 3:
        num_max = num
print('Ваше число', num, 'Угадал за ', score, 'попыток.')
