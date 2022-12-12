"""
Задача 1. Права доступа
Что нужно сделать
Перед вами стоит задача создать и поддерживать специализированный форум. Вы только приступили и сейчас работаете над
действиями, которые могут совершать посетители форума. Для разных пользователей прописаны разные возможности.
Напишите декоратор check_permission, который проверяет, есть ли у пользователя доступ к вызываемой функции,
и если нет, то выдаёт исключение PermissionError.

Пример кода:
user_permissions = ['admin']
@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')
delete_site()
add_comment()

Результат:
Удаляем сайт
PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию add_comment
"""

import functools
from _collections_abc import Callable

def check_permission(_func = None, *, name: str = None):
    def permission(func: Callable) -> Callable:

        """Проверяет есть у пользователя доступ,
        если нет то выдаем исключение"""
       
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            try:
                if name in user_permissions:
                    result = func(*args, **kwargs)
                    return result
                else:
                    raise PermissionError
            except PermissionError:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
        return wrapped_func
    return permission

@check_permission(name='admin')
def delete_site():
    """Удаляет сайт"""
    print('Удаляем сайт')

@check_permission(name='user_1')
def add_comment():
    """Добавляет комментарий"""
    print('Добавляем комментарий')

user_permissions = ['admin']
delete_site()
add_comment()