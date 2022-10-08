"""
Задача 5. Недоделка 2
Что нужно сделать

Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого горе-программиста.
В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код по следующим
условиям: программа получает на вход два числа. В первом числе должно быть не меньше трёх цифр, во втором
числе — не меньше четырёх, иначе программа выдаёт ошибку. Если всё нормально, то в каждом числе первая и
последняя цифра меняются местами, а затем выводится их сумма.
И тут вы натыкаетесь на программу, которая была написана прошлым программистом и которая как раз решает такую задачу!
Однако старший программист сказал вам немного переписать этот код, чтобы он не выглядел так ужасно.
Да и вам самим становится, мягко говоря, не по себе от него.
Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше.
Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.
first_n = int(input("Введите первое число: "))
first_num_count = 0
temp = first_n
while temp > 0:
    first_num_count += 1
    temp = temp // 10
if first_num_count < 3:
 print("В первом числе меньше трёх цифр.")
else:
 last_digit = first_n % 10
 first_digit = first_n // 10 ** (first_num_count - 1)
 between_digits = first_n % 10 ** (first_num_count - 1) // 10
 first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
 print('Изменённое первое число:', first_n)
 second_n = int(input("\nВведите второе число: "))
 second_num_count = 0
 temp = second_n
 while temp > 0:
   second_num_count += 1
   temp = temp // 10
 if second_num_count < 4:
   print("Во втором числе меньше четырёх цифр.")
 else:
   last_digit = second_n % 10
   first_digit = second_n // 10 ** (second_num_count - 1)
   between_digits = second_n % 10 ** (second_num_count - 1) // 10
   second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
   print('Изменённое второе число:', second_n)
   print('\nСумма чисел:', first_n + second_n)
"""

def number_processing(numb, x):
    if len(str(numb)) != x:
        print('В этом числе должно быть', x, 'цифр')
    else:
        first_n = numb // 10 ** (x - 1)
        last_n = numb % 10
        midle_n = (numb % 10 ** (x - 1)) // 10
        new_number = (last_n * 10 ** (x - 1)) + midle_n * 10 + first_n
        return new_number

number_1 = int(input("Введите первое число: "))
one_numb = number_processing(number_1, 3)
number_2 = int(input("Введите первое число: "))
two_numb = number_processing(number_2, 4)
print('Изменённое первое число:', one_numb, '\nИзменённое второе число:', two_numb, '\nСумма чисел:', one_numb + two_numb)






