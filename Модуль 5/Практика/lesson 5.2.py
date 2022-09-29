"""
Задача 1. Координаты

Мы тестируем 2D-игру, где нужно управлять подводной лодкой. У лодки есть координаты в
пространстве — X (икс) и Y (игрек). X — это движение вперёд-назад, а Y —  вверх-вниз.
Соответственно, во время движения лодки меняются и её координаты. Во время тестирования
игры нам необходимо сравнивать эти координаты и выводить на экран нужное сообщение, в том числе если они равны.
Вводятся две координаты — X и Y. С помощью трёх последовательных проверок сравните
обе координаты и выведите соответствующее сообщение.

Пример:
Введите икс: 5
Введите игрек: 6
X меньше Y

Пример 2:
Введите икс: 3
Введите игрек: 3
X равен Y

Задача 2. Скидки!

Напишите программу для примера, разобранного в уроке. Пользователь покупает курс
стоимостью 75 000 рублей. Если денег на счету достаточно, то нужно:
Списать со счёта деньги.
Проверить баланс счёта. Если там меньше 5000 рублей, то зачислить на счёт 1000 рублей и вывести сообщение: «Сделана скидка».
Вывести сообщение: «Курс успешно приобретён».
А иначе вывести: «Не хватает денег на счету». Также в конце вывести остаток счёта и сообщение: «Хорошего дня!»

Пример:
Сколько денег на счету? 78500
Курс успешно приобретён
Сделана скидка
Остаток на счету: 4500
Хорошего дня!

Задача 3

Мама дала Маше денег и отправила её в магазин за сыром. А ещё сказала: «Если останутся деньги,
 то можешь купить себе мороженое. Если денег на сыр не хватит, то денег маловато — а значит, и мороженого не будет».
Сделайте программу, которая получает на вход количество денег. Сыр стоит 60 рублей,
мороженое — 20 рублей. Если денег на сыр хватает (больше либо равно), то:
Выводите сообщение: «На сыр денег хватило», — и вычитайте стоимость сыра из кошелька.
Если оставшихся денег хватает на мороженое, то выводите: «И на мороженое тоже!». Иначе выводите: «Денег маловато».
"""

# Задача 1
print('=' * 40)
print('Задача 1')
x = int(input('Введите х: '))
y = int(input('Введите y: '))
if x != y:
    if x > y:
        print('x больше y')
    else:
        print('x меньше y')
else:
    print('x равен y')

# Задача 2
print('=' * 40)
print('Задача 2')
money = int(input('Сколько денег на счету? '))
price = 75000
if money >= price:
    money -= price
    print('Курс успешно приобретён')
    if money < 5000:
        money += 1000
        print('Сделана скидка')
else:
    print('Недостаточно денег.')
print('Остаток на счету:', money)
print('Хорошего дня!')

# Задача 3
print('=' * 40)
print('Задача 3')
price_cheece = 60
price_ice_cream = 20
money = int(input('Введите сумму, сколько дала мама Маше: '))
if money >= price_cheece:
    print('На сыр денег хватило')
    money -= price_cheece
    if money >= price_ice_cream:
        print('И на мороженое тоже!')
        money -= price_ice_cream
    else:
        print('Денег маловато')
else:
    print('Денег маловато')
print('Осталось денег:', money)






















