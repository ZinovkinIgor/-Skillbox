"""
Задача 1. Бесконечный итератор
Реализуйте итератор-счётчик, который не принимает никаких атрибутов и имеет только один статический атрибут — счётчик.
Итератор увеличивает счётчик и возвращает предыдущее значение. У вас должен получиться бесконечный итератор.

То есть при вызове такого кода в основной программе
my_iter = СountIterator()
for i_elem in my_iter:
    print(i_elem)
значения будут выдаваться бесконечно.

Задача 2. Случайная сумма
Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов. Каждый новый элемент —
это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента (первый элемент — просто случайное
вещественное число от 0 до 1). Алексею нельзя хранить в памяти весь этот список, а со значениями работать как-то надо.

Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу. Также сделайте, чтобы при каждом новом вызове
итератора в цикле значения считались заново.

Пример работы программы:
Кол-во элементов: 5
Элементы итератора:
0.74
1.13
1.95
2.2
2.55
Новое кол-во элементов: 6
Элементы итератора:
0.79
1.58
2.55
2.81
3.06
3.34

Задача 3. Простые числа
Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.

Основной код:
prime_nums = Primes(50)
for i_elem in prime_nums:
    print(i_elem, end=' ')
Ожидаемый результат кода:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
"""
import random
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    class CountIterator:
        def __init__(self):
            self.count = 0

        def __iter__(self):
            return self

        def __next__(self):
            self.count += 1
            return self.count


    my_iter = CountIterator()
    for i_elem in my_iter:
        print(i_elem)


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    class RandomNumber:
        def __init__(self, count):
            self.numb = 0
            self.summ = 0
            self.score = 0
            self.count = count


        def __iter__(self):
            self.numb = 0
            self.summ = 0
            self.score = 0
            return self

        def __next__(self):
            if self.count > self.score:
                self.score += 1
                randon_float = round(random.uniform(0, 1), 2)
                self.summ += randon_float
                return (round(self.summ, 2))
            else:
                raise StopIteration

    score = int(input('Введите количество итераций: '))
    my_numb = RandomNumber(score)
    for numb in my_numb:
        print(numb)

    for numb in my_numb:
        print(numb)


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


    class Primes:

        def __init__(self, scor):
            self.numbers = []
            self.scor = scor
            self.num = 0

        def __iter__(self):
            return self

        def __next__(self):
            k = 0
            for i_num in range(2, self.scor + 1):
                self.num += 1
                if self.num > self.scor:
                    raise StopIteration
                for i in range(2, i_num):
                    if i_num % i == 0:
                        k = k + 1
                if k == 0:
                    self.numbers.append(i_num)
                else:
                    k = 0
            for i_elem in self.numbers:
                print(i_elem, end=' ')


    prime_nums = Primes(50)
    next(prime_nums)


else:
    print('Выберите задачу заново.')

