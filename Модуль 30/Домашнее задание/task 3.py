"""
Задача 3. Палиндром: возвращение
Что нужно сделать
Есть множество встроенных и внешних библиотек для работы с данными в Python.
С некоторыми из них вы уже работали. Например, с модулем collections,
когда использовали специальный класс OrderedDict, с помощью которого делали упорядоченный словарь.
В этой библиотеке есть и другие возможности, но их немного. Официальная документация: collections — Container datatypes.

Используя модуль collections, реализуйте функцию can_be_poly, которая принимает на вход строку и проверяет,
можно ли получить из неё палиндром.

Пример кода:

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
Результат:
True
False
"""

from collections import Counter

def can_be_poly(word: str) -> bool:
    result = Counter(word)
    num = 0
    for key, value in result.items():
        if value % 2 != 0:
            num += 1
    if num > 1:
        return False
    else:
        return True

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))