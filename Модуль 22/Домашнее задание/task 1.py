"""
Задача 1. Сумма чисел 2
Что нужно сделать

Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены пробелами и концами строк. Напишите программу,
которая выводит сумму чисел в выходной файл answer.txt.

Пример:
Содержимое файла numbers.txt
     2
2
  2
        2
Содержимое файла answer.txt
8
"""
summ = 0
number = open('numbers.txt', 'r')
for numb in number:
    summ += int(numb)
answer = open('answer.txt', 'w')
answer.write(str(summ))
number.close()
answer.close()

