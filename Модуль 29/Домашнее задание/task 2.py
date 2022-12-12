"""
Задача 2. Функция обратного вызова
Что нужно сделать
При работе с сетью и веб-сервисами иногда используется функция callback, так называемая функция обратного вызова.
Это функция, которая вызывается при срабатывании определённого события: переходе на страницу, получении сообщения
или окончании обработки процессором. В неё можно передать функцию, чтобы она выполнилась после определённого события.
Это используется, например, в HTTP-серверах в ответ на URL-запросы. Реализуйте такую функцию.

Пример функции:

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

Основной код:
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
Ожидаемый результат: пример функции, которая возвращает ответ сервера.
Ответ: OK.

Подсказка: функция callback, в зависимости от условия, может быть вызвана следующим действием или просто так.
"""

from _collections_abc import Callable
import functools


def callback(_func=None, *, adress: str=None):
    def open_file(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if adress in app:
                result = func(*args, **kwargs)
                return result
        return wrapped
    return open_file


@callback(adress='//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

"""
route - это переменная которая вызывает функцию
app функция в которой хранится словарь
"""


app = {'//': example}

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')