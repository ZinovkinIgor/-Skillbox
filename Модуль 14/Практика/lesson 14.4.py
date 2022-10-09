"""
Задача 1. Настройка
Вы устроились Python-разработчиком, и на новом рабочем месте уже стоит PyCharm. Конечно же, прежде чем начать работать
с кодом, вы хотите настроить его под себя, чтобы чувствовать себя как дома.
Перейдите в настройки PyCharm (File — Settings — Editor) и настройте среду разработки:
Сделайте так, чтобы размер шрифта увеличивался при помощи комбинации Ctrl + колесо мыши.
В разделе Font выберите наиболее подходящий вам стиль текста.
В разделе Color Scheme выберите подходящий цвет IDE.
Найдите раздел, который отвечает за стиль кода в Python, и сравните с тем, что мы писали раньше.

Задача 2. НОД
Помните, мы писали функцию, которая находит наибольший общий делитель двух чисел? Вот этот код:

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print('Наибольший общий делитель:', a + b)

gcd(30, 18)
Теперь представьте ситуацию, что вам нужно объяснить другому человеку, как этот код работает, шаг за шагом.
Предположим, на вход подаются числа 4782 и 698. Используя только точку останова, определите, чему будет равняться
переменная а, когда переменная b станет равна двум.

Задача 3. Сессия
Для сдачи зачёта студент Пётр написал программу, которая по координатам двух точек определяет уравнение прямой,
проходящей через эти две точки, в виде y = k * x + b, где k и b — числа, означающие угловой коэффициент и вертикальное
смещение прямой. Вот текст этой программы:

print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
k = y_diff / x_diff
b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)

Пример работы программы (содержимое консоли):
Введите первую точку
X: 10
Y: 20
Введите вторую точку
X: 15
Y: 25
Уравнение прямой, проходящей через эти точки:
y =  1.0 * x +  10.0

Однако вечером накануне сдачи Пётр обнаружил, что программа не всегда работает правильно. Например,
она не выдаёт корректное уравнение, если координаты первой точки равны (10, 20), а координаты второй
точки равны (10, 45). Отчаявшись и предвидя бессонную ночь, Пётр обратился к вам за помощью. Помогите
ему найти и исправить ошибку в коде с помощью брейк-поинтов, чтобы уравнение прямой составлялось правильно
во всех случаях. Используйте PyCharm.
"""

# Задача 1
print('=' * 40)
print('Задача 1')

# Задача 2
print('=' * 40)
print('Задача 2')
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print('Наибольший общий делитель:', a + b)
gcd(4782, 698)

# Задача 3
print('=' * 40)
print('Задача 3')
print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))
x_diff = x1 - x2
y_diff = y1 - y2

if x_diff == 0:
    print('Прямая параллельна оси Y')
elif y_diff == 0:
    print('Прямая параллельна оси X')
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b)




