"""
Задача 7. Годы
Что нужно сделать

Недавно Костя прочитал научно-фантастическую книгу. В ней самые страшные события случались только тогда,
когда в году были три одинаковые цифры. Косте стало интересно, какие годы были или будут «особенными» в определённом промежутке.
Напишите программу, в которой у пользователя запрашивается два четырёхзначных числа A и B. Затем выведите в
порядке возрастания все четырёхзначные числа в интервале от A до B, запись которых содержит ровно три одинаковые цифры.

Пример работы программы:
Введите первый год: 1900
Введите второй год: 2100
Годы от 1900 до 2100 с тремя одинаковыми цифрами:
1911
1999
2000
2022
"""

def year(min_year, max_year):
    for numb in range(min_year, max_year + 1):
        for n in str(numb):
            score = 0
            for simb in str(numb):
                if n == simb:
                    score += 1
            if score == 3:
                print(numb)
                break

min_year = int(input('Введите первый год: '))
max_year = int(input('Введите второй год: '))
print('Годы от 1900 до 2100 с тремя одинаковыми цифрами:')
year(min_year, max_year)




