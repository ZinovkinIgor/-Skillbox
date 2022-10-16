"""
Задача 5. Гистограмма частоты 2
Что нужно сделать
Мы уже писали программу для лингвистов, которая получала на вход текст и считала, сколько раз в строке встречается каждый символ.
Теперь задача немного поменялась: максимальную частоту выводить не нужно, однако необходимо написать функцию,
которая будет инвертировать полученный словарь. То есть в качестве ключа будет частота, а в качестве значения — список
символов с этой частотой. Реализуйте такую программу.

Пример:
Введите текст: здесь что-то написано
Оригинальный словарь частот:
  : 2
- : 1
З : 1
а : 2
д : 1
е : 1
и : 1
н : 2
о : 3
п : 1
с : 2
т : 2
ч : 1
ь : 1

Инвертированный словарь частот:
1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
2 : ['с', ' ', 'т', 'н', 'а']
3 : ['о']
"""

simbol_dict = dict()
new_simbol_dict = dict()
text = input('Введите текст: ').lower()
for sim in text:
    if sim not in simbol_dict:
        simbol_dict[sim] = 1
    else:
        simbol_dict[sim] += 1

for num in sorted(simbol_dict):
    print(num, ':', simbol_dict[num])
    if simbol_dict[num] not in new_simbol_dict:
        new_simbol_dict[simbol_dict[num]] = []
        new_simbol_dict[simbol_dict[num]].append(num)
    else:
        new_simbol_dict[simbol_dict[num]].append(num)

print(simbol_dict)
for i_num in sorted(new_simbol_dict):
    print(i_num, ':', new_simbol_dict[i_num])