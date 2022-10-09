"""
Задача 4. Видеокарты
Что нужно сделать
В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений. Вместо полных названий хранятся
только числа, которые обозначают модель и поколение видеокарты. Недавно компания выпустила новую линейку видеокарт.
Самые старшие поколения разобрали за пару дней.
Напишите программу, которая удаляет из списка видеокарт наибольшие элементы.

Пример:
Количество видеокарт: 5
1 Видеокарта: 3070
2 Видеокарта: 2060
3 Видеокарта: 3090
4 Видеокарта: 3070
5 Видеокарта: 3090

Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
Новый список видеокарт: [ 3070 2060 3070 ]
"""
nvidia_list = []
new_nvidia_list = []

score = int(input('Количество видеокарт: '))
for num in range(score):
    print(num + 1, 'Видеокарта: ', end='')
    new_card = int(input())
    nvidia_list.append(new_card)
max_num = nvidia_list[0]
for index in range(len(nvidia_list)):
    if max_num < nvidia_list[index]:
        max_num = nvidia_list[index]
for index in range(len(nvidia_list)):
    if max_num != nvidia_list[index]:
        new_nvidia_list.append(nvidia_list[index])
print('Старый список видеокарт:', nvidia_list)
print('Новый список видеокарт:', new_nvidia_list)