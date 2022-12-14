"""
Задача 10. Своя функция zip
Что нужно сделать

В самом конце собеседования вас неожиданно спросили: «Расскажите, что делает функция zip?». Чтобы произвести впечатление,
вы решили не только рассказать про неё, но и написать её аналог.
Даны строка и кортеж из чисел. Напишите программу, которая создаёт генератор из пар кортежей «символ — число».
Затем выведите на экран сам генератор и кортежи.

Пример:
Строка: abcd
Кортеж чисел: (10, 20, 30, 40)

Результат:
<generator object <genexpr> at 0x00000204A4234048>
('a', 10)
('b', 20)
('c', 30)
('d', 40)

Дополнительно: создайте полный аналог функции zip — сделайте так, чтобы программа работала с любыми итерируемыми типами данных.
"""

def func(number):
    for n in range(number):
        print(f'(\'{word[n]}\', {numb_tuple[n]})')

word = 'abcdy'
numb_tuple = (10, 20, 30, 40, 80)
if len(word) > len(numb_tuple):
    func(len(numb_tuple))
else:
    func(len(word))

new_tuple = zip(word, numb_tuple)
print(new_tuple)
for n in new_tuple:
    print(n)
