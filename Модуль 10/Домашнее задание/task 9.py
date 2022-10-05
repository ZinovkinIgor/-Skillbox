"""
Задача 9. Пирамидка 2
Что нужно сделать

Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами вот так:
"""
number = int(input('Введите уровень пирамиды: '))
num = 1
for scor in range(1, number + 1):
  if scor == 1:
    print('\t' * (number - 1) + str(num), end='')
  else:
    print('\t' * (number - scor), end='')
    for scor2 in range(1, scor + 1):
      num += 2
      print(str(num), '\t', end='\t')
  print()

print('=' * 20, 'ИЛИ', '=' * 20)
new_num = 1
for line in range(number):
  for spece in range(number - line - 1, 0, -1):
    print(end='   ')
  for numb in range(line + 1):
    print(new_num, end='    ')
    new_num += 2
  print()

print('=' * 20, 'ИЛИ', '=' * 20)
new_num = 1
for line in range(number):
  spece_count = number - line - 1
  print('   ' * spece_count, end='')
  for numb in range(line + 1):
    print(new_num, end='    ')
    new_num += 2
  print()
