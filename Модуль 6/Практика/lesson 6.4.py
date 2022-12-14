"""
Что нужно сделать
Задача 1. Неправильный таймер

Петя писал таймер для телефона, но у него что-то пошло не так.

count = 0
While count <= 10
 if count == 0:
   print('Время вышло!')
 else:
   print(count)
   count -= 1

Скопируйте программу в редактор, исправьте ошибки и убедитесь, что на экран выводятся числа с 10 до 0 и сообщение «Время вышло!».

Задача 2. Тестируем приложение

Напишите программу, которая имитирует работу с приложением: программа спрашивает у пользователя «Продолжаем работать?
1/0: » до тех пор, пока пользователь не введёт 0, — после этого выводится сообщение: «Приложение закрывается…».
В конце программы также выводится сообщение: «Работа завершена». Для создания бесконечного цикла используйте while True.

Задача 3. Вирус

Дима написал программу-вирус специально для того, чтобы проучить своего друга-должника, который никак не хочет возвращать скейтборд.
Программа не даёт работать за компьютером и постоянно выводит на экран сообщение «Компьютер заблокирован.
Вернёшь скейт — скажу код разблокировки!». Как только вводится правильный код, вирус удаляется.
Напишите такую же программу, которую написал Дима.

Пример:
Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
Введите код: 1005
Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
Введите код: 7777
Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
Введите код: 0550
Код верный, завершаю работу...
"""

# Задача 1
print('=' * 40)
print('Задача 1')
count = 10
while count <= 10:
 if count == 0:
   print('Время вышло!')
   break
 else:
   print(count)
   count -= 1

# Задача 2
print('=' * 40)
print('Задача 2')
while True:
    answer = int(input('Продолжаем работать? 1/0 '))
    if answer == 0:
        print('Приложение закрывается…')
        break
print('Работа завершена')


# Задача 3
print('=' * 40)
print('Задача 3')
while True:
    print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
    code = input('Введите код: ')
    if code == '0550':
        print('Код верный, завершаю работу...')
        break
