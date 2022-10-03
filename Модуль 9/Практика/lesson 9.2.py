"""
Задача 1. Урок литературы
Выполните задание, разобранное в уроке.

К уроку литературы нужно было прочитать “Евгения Онегина”. Учитель задаёт вопрос пяти случайным детям.
Она задаёт вопрос “Кто написал произведение?” и если ученик не угадывает, то учитель ставит двойку и
спрашивает следующего. Если хоть кто-то угадает, то вопросы больше не задаются. Напишите программу,
которая посчитает количество двоечников из этих пяти.

Задача 2. Начальник
Напишите программу для робота-начальника. Он спрашивает у пользователя, выполнил ли он задание, которые выдавал вчера,
и продолжает это делать до тех пор, пока тот не ответит ему “Да, конечно, сделал”.

Задача 3. Дразнилка.
Напишите программу-дразнилку “Купи слона”. Она спрашивает у пользователя, как его зовут, затем отвечает “%username%,
купи слона”. Дальше, что бы он ни говорил, она передразнивает: Все говорят “...”, а ты купи слона!

Пример:
Как тебя зовут? Дима
Дима, купи слона!
Хорошо, давай куплю
Все говорят Хорошо, давай куплю, а ты купи слона!
...
"""
# Задача 1
print('=' * 40)
print('Задача 1')
ball_count = 0
for _ in range(5):
    answer = input('Кто написал “Евгения Онегина”: ')
    if answer == 'Пушкин' or answer == 'пушкин':
        print('Молодец')
        break
    print('Неправильно! Два.')
    ball_count += 1
print('Двоек получили:', ball_count)

# Задача 2
print('=' * 40)
print('Задача 2')
while True:
    answer = input('Ты выполнил задание, которые выдавал вчера: ')
    if answer == 'Да, конечно, сделал':
        break
print('Хорошо!')

# Задача 3
print('=' * 40)
print('Задача 3')
name = input('Привет, как тебя зовут? ')
print(name, 'купи слона!')
while True:
    answer = input()
    print('Все говорят', answer + ', а ты купи слона!')

