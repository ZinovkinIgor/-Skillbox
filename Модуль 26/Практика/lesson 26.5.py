"""
Задача 1. Бесконечный генератор
По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой счётчик-генератор,
который также в цикле будет бесконечно выдавать значения.
Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.

Задача 2. Очень большой файл
Вам на обработку пришёл огромнейший файл с данными. Настолько огромный, что при его открытии компьютер просто зависает,
так как данные не помещаются в оперативной памяти вашего суперкомпьютера (не очень-то и «супер»).

В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки. Напишите программу,
которая подсчитает общую сумму чисел в файле. Для считывания файла реализуйте специальный генератор.
"""
import random

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    def number_count(count):

        for numb in range(2, count + 1):
            k = False
            for scor in range(2, numb):
                if numb % scor == 0:
                    k = True
                    break
            if k == False:
                yield numb

    numb = number_count(10000)
    for n in numb:
        print(n, end=' ')


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')


    """
    Создаем генератором numbers.txt рандомные цифры от 1 до 1000
    в каждой строке по 10 чисел.
    """
    def new_numb_list():
        for _ in range(500):
            res = random.randint(1, 1000)
            print(res)
            yield res

    with open('numbers.txt', 'a', encoding='utf-8') as file:
        scor = 0
        while scor < 500:

            if scor % 10 == 0:
                file.write('\n')
            res = (f'{new_numb_list().__next__()} ')
            file.write(''.join(str(res)))
            scor += 1

elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

    def summ_numbers(file):
        with open(file) as number:
            for numb in number.read().split():
                yield int(numb)


    result = summ_numbers('numbers.txt')
    summ = 0
    for n in result:
        summ += n
    print(summ)

else:
    print('Выберите задачу заново.')



