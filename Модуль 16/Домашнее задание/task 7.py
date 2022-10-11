"""
Задача 7. Ролики
Что нужно сделать
Частная контора даёт в прокат ролики самых разных размеров. Человек может надеть ролики любого размера,
которые не меньше размера его ноги.
Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей. Реализуйте код,
который определяет, какое наибольшее число человек сможет одновременно взять ролики и пойти покататься.

Пример:
Кол-во коньков: 4
Размер 1-й пары: 41
Размер 2-й пары: 40
Размер 3-й пары: 39
Размер 4-й пары: 42

Кол-во людей: 3
Размер ноги 1-го человека: 42
Размер ноги 2-го человека: 41
Размер ноги 3-го человека: 42

Наибольшее кол-во людей, которые могут взять ролики: 2
"""


skates_list, human_list = [], []
count = 0
skates = int(input('Кол-во коньков: '))
for num in range(1, skates + 1):
    print('Размер', str(num) + '-й пары: ', end='')
    couple = int(input())
    skates_list.append(couple)
human = int(input('\nКол-во людей: '))
for num in range(1, human + 1):
    print('Размер ноги', str(num) + '-го человека: ', end='')
    foot_size = int(input())
    human_list.append(foot_size)

skates_list.sort()
human_list.sort(reverse=True)

for human_search in human_list:
    for skates_search in skates_list:
        if human_search <= skates_search:
            human_list.remove(human_search)
            skates_list.remove(skates_search)
            count += 1
            break
print('Наибольшее кол-во людей, которые могут взять ролики:', count)


