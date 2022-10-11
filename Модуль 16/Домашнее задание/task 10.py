"""
Задача 10. Симметричная последовательность
Что нужно сделать
Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево.
Например, следующие последовательности являются симметричными:
1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1
Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет, какое минимальное
количество и каких чисел надо приписать в конец этой последовательности, чтобы она стала симметричной.

Пример 1:
Кол-во чисел: 5
Число: 1
Число: 2
Число: 1
Число: 2
Число: 2

Последовательность: [1, 2, 1, 2, 2]
Нужно приписать чисел: 3
Сами числа: [1, 2, 1]

Пример 2:
Кол-во чисел: 5
Число: 1
Число: 2
Число: 3
Число: 4
Число: 5

Последовательность: [1, 2, 3, 4, 5]
Нужно приписать чисел: 4
Сами числа: [4, 3, 2, 1]
"""

def is_polindrom(new_list):
    new_revers = []
    for i_scor in range(len(new_list) -1, - 1, -1):
        new_revers.append(new_list[i_scor])
    if new_list == new_revers:
        return True
    else:
        return False

score = int(input('Кол-во чисел: '))
numbers = []
new_numbers = []
answer = []

for _ in range(score):
    numbers.append(int(input('Число: ')))

for i_num in range(len(numbers)):
    for i_tem in range(i_num, len(numbers)):
        new_numbers.append(numbers[i_tem])
    if is_polindrom(new_numbers):
        for num in range(0, i_num):
            answer.append(numbers[num])
        answer.reverse()
        break
    new_numbers = []
print(numbers)
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)



print('\n\n\ИЛИn\n')
score = int(input('Кол-во чисел: '))
numbers = []

for _ in range(score):
    numbers.append(int(input('Число: ')))

counter = 0
while numbers != numbers[::-1]:
    numbers.insert(score, numbers[counter])
    counter += 1

print('Нужно приписать чисел:', counter)
print('Сами числа:', numbers[:counter][::-1])

