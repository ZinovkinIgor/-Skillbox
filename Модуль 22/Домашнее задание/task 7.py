"""
Задача 7. Турнир
Что нужно сделать

В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре «Орлеан»: фамилии,
имена и количество баллов, набранных в первом туре. Во второй тур проходят участники, которые набрали более K баллов в первом туре.
Напишите программу, которая выводит в файл second_tour.txt данные всех участников, прошедших во второй тур, с нумерацией.
В первой строке нужно вывести в файл second_tour.txt количество участников второго тура. Затем программа должна
вывести фамилии, инициалы и количество баллов всех участников, прошедших во второй тур, с нумерацией.
Имя нужно сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.

Пример:
Содержимое файла first_tour.txt:
80
Ivanov Serg 80
Segeev Petr 92
Petrov Vasiliy 98
Vasiliev Maxim 78

Содержимое файла second_tour.txt:
2
1) V. Petrov 98
2) P. Sergeev 92
"""


"""
открываем файл и сохраняем всех участников в новый словарь, 
далее сортируем словарь по значению
"""

# раскрываем скобки
def func_name(name):
    res = ''
    for n in name:
        res += n
    return res

players_dict = dict()
text = open('first_tour.txt', 'r')
k = text.read(3)
players = text.read().split('\n')

for name in players:
    simb_names = name.split()[1][0] + '.'
    players_dict[simb_names, name.split()[0]] = name.split()[2]

list_final = [numb for numb in sorted(players_dict.values(), reverse=True) if numb >= k]

# Выводим на экран результат и сохраняем в новый файл.
new_file = open('second_tour.txt', 'a')
for scor, count in enumerate(list_final):
    for name, numb in players_dict.items():
        if count == numb:
            print('{}) {} {}'.format(scor + 1, func_name(name), numb))
            new_file.write('{}) {} {}\n'.format(scor + 1, func_name(name), numb))

new_file.close()
text.close()



