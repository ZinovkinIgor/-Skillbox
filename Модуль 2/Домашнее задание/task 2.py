"""
Задача 2. Цвета
Что нужно сделать

Исправьте программу так, чтобы в результате её выполнения на экран в одну строку выводился текст:
Red Blue Green RedGreenBlue Blue GreenBlue.

r = 'Red'
g = 'Green'
b = 'Blue'

print(b, r, g, b, g + b, b + b + g, b)

Что оценивается

Результат вывода соответствует картинке (тексту).
После запятой стоит пробел, перед запятой пробела нет.
Знак конкатенации (+) выделен пробелами с двух сторон.
"""
print('Red Blue Green RedGreenBlue Blue GreenBlue')

r = 'Red'
g = 'Green'
b = 'Blue'

print(r, b, g, r + g + b, b, g + b)