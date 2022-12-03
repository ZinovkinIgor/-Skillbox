"""
Задача 4. Последовательность Хофштадтера
Что нужно сделать

Реализуйте генерацию последовательности Q Хофштадтера (итератором или генератором). Сама последовательность выглядит так:

Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2))
В итератор (или генератор) передаётся список из двух чисел. Например, QHofstadter([1, 1]) генерирует точную
последовательность Хофштадтера. Если передать значения [1, 2], то последовательность должна немедленно завершиться.

"""

class Qsequence:
    def __init__(self, s):
        self.s = s[:]

    def __next__(self):
        try:
            if self.s == [1, 2]:
                raise StopIteration
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            print('Выражение: {}+{} = {}'.format(self.s[-self.s[-1]], self.s[-self.s[-2]], q))
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self):
        return self.s

Q = Qsequence([1, 1])
for _ in range(10):
    print(next(Q))

#
# [next(Q) for __ in range(10)]
# [3, 4, 5, 5, 6, 6, 6, 8, 8, 8]