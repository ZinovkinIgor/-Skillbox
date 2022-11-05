"""
Задача 5. Текстовый калькулятор
Что нужно сделать
Иван стоит на пороге величайшего открытия (не будем его расстраивать), которое перевернёт представление о
всей математике и программировании. Имя этому открытию — текстовый калькулятор. Правда, код для своего
открытия ему сложно написать самому, и поэтому он попросил вас помочь ему. Так что уже можно бежать в патентное бюро.

Есть файл calc.txt, в котором хранятся записи вида
100 + 34
23 / 4
то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделённые пробелами.

Операнды — целые числа. Операции — арифметические (включая деление нацело и нахождение остатка).
Напишите программу, которая вычисляет все эти операции и находит сумму их результатов. Пропишите обработку возможных ошибок.
Программа не должна завершаться при первой же ошибке, она учитывает все верные строки и выводит найденный ответ.
После успешного выполнения задания, попробуйте модифицировать задачу. Теперь пользователю на экран должно выводиться
сообщение с ошибочной строкой и предложением её исправить.

Пример 1
Содержимое файла calc.txt:
100 + 34
10 +* 3
23 / 4

Содержимое консоли:
Обнаружена ошибка в строке: 10 +* 3   Хотите исправить? Да
Введите исправленную строку: 10 + 3

Сумма результатов: 152.75

Пример 2
Содержимое файла calc.txt:
100 + 34
10 +* 3
20 -* 2
23 / 4

Содержимое консоли:
Обнаружена ошибка в строке: 10 +* 3   Хотите исправить? Нет
Обнаружена ошибка в строке: 20 -* 2   Хотите исправить? Да
Введите исправленную строку: 20 - 2

Сумма результатов: 157.75
"""
def error_example(operand_1, action, operand_2):
    res = input('Обнаружена ошибка в строке {} {} {}. Хотите ее исправить? '.format(operand_1, action, operand_2))

def decision(example, scor):
    '''
    берем строку и делем ее на  операнды и операции
    проводим арифметические действия,
    проводим работу с исключениями.
    '''
    answer = 0
    numbers = example.split()
    operand_1, action, operand_2 = int(numbers[0]), numbers[1], int(numbers[2])
    try:

        if action == '+':
            answer = operand_1 + operand_2
        elif action == '-':
            answer = operand_1 - operand_2
        elif action == '*':
            answer = operand_1 * operand_2
        elif action == '/':
            answer = operand_1 / operand_2
        elif action == '//':
            answer = operand_1 // operand_2
        elif action == '%':
            answer = operand_1 % operand_2
        # else:
        #     raise UnboundLocalError
        print(f'{operand_1} {action} {operand_2} = {answer}')
    except IndexError:
        print(f'Строка {scor}. Выражение должно состоять из 3 значений.')
        result = error_example(operand_1, action, operand_2)
        return result
    except ValueError:
        print(f'Строка {scor}. Операнд не является целым числом.')
        result = error_example(operand_1, action, operand_2)
        return result
    except UnboundLocalError:
        print(f'Строка {scor}. Операция введена не верно.')
        result = error_example(operand_1, action, operand_2)
        return result

    return answer


scor = 0
summ = 0
with open('calc.txt', 'r') as library:
    for example in library:
        scor += 1
        result = decision(example, scor)

        summ += result
    print('Сумма всех верных выражений: {}'.format(summ))