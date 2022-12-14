"""
Задача 7. Ход конём
Что нужно сделать

В рамках разработки шахматного ИИ стоит новая задача. По заданным вещественным координатам коня и второй точки
программа должна определить может ли конь ходить в эту точку. Используйте как можно меньше конструкций if и
логических операторов. Обеспечьте контроль ввода.

Пример:
Введите местоположение коня:
0.071
0.118
Введите местоположение точки на доске:
0.213
0.068
Конь в клетке (0, 1). Точка в клетке (2, 0).
Да, конь может ходить в эту точку.
"""
while True:
    print('Введите местоположение коня:')
    point_x = float(input('Точка x: '))
    point_y = float(input('Точка y: '))
    print('Введите местоположение точки на доске:')
    new_point_x = float(input('Точка x: '))
    new_point_y = float(input('Точка y: '))

    x = int(point_x * 10)
    y = int(point_y * 10)
    new_x = int(new_point_x * 10)
    new_y = int(new_point_y * 10)

    if 0 < x > 9 or 0 < y > 9 or 0 < new_x > 9 or 0 < new_y > 9:
        print('Вы вышли за диапазон шахматной доски')
        continue

    dx = abs(x - new_x)
    dy = abs(y - new_y)
    print('Конь в клетке (' + str(x) + ', ' + str(y) + '). Точка в клетке (' + str(new_x) + ', ' + str(new_y) + ').')
    if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
        print('Да, конь может ходить в эту клетку.')
    else:
        print('Нет, конь так не ходит.')






