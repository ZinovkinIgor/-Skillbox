"""
Задача 4. Регистрация
Что нужно сделать

У вас есть файл с протоколом регистраций пользователей на сайте — registrations.txt. Каждая строка содержит:
ИМЯ ИМЕЙЛ ВОЗРАСТ, разделённые пробелами. Например: Василий test@test.ru 27

Напишите программу, которая проверяет данные из файла для каждой строки:

Присутствуют все три поля.
Поле имени содержит только буквы.
Поле «Имейл» содержит @ и . (точку).
Поле «Возраст» является числом от 10 до 99.
В результате проверки сформируйте два файла:

registrations_good.log — для правильных данных, записывать строки как есть,
registrations_bad.log — для ошибочных, записывать строку и вид ошибки.
Для валидации строки данных напишите функцию, которая может выдавать исключения:

НЕ присутствуют все три поля: IndexError.
Поле имени содержит НЕ только буквы: NameError.
Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.
Поле «Возраст» НЕ является числом от 10 до 99: ValueError.

Формат выходных данных
Содержимое файла registrations_bad.log:
Ольга kmrn@gmail.com 123        Поле «Возраст» НЕ является числом от 10 до 99
Чехова kb@gmail.com 142        Поле «Возраст» НЕ является числом от 10 до 99
……
Степан ky 59        Поле «Имейл» НЕ содержит @ и . (точку)
……

Содержимое файла registrations_good.log:
Геннадий ttdababmt@gmail.com 69
Ольга ysbxur@gmail.com 20
……

"""


def chek_registrations(human, scor):
    '''
    идем по строкам каждую строку делим на имя, почту, возраст
    запускаем функцию по проверке имени,почты, возраста.
    если есть ошибки, то строка записывается в  файл-ошибки с указанием типа ошибки, иначе в результат идет в файл-ответ
    '''
    try:
        names = human.split()
        name, mail, year = names[0], names[1], names[2]
        try:
            if name.isalpha():
                if '@' and '.' in mail:
                    if 10 < int(year) < 99:
                        registrations_good.write(f'name {name}\t\t mail {mail}\t\t year {year}\n')
                    else:
                        raise ValueError
                else:
                    raise SyntaxError
            else:
                raise NameError
        except NameError:
            registrations_bad.write(
                '{human} \t\t В строке {scor} ошибка NameError. В поле имени содержит НЕ только буквы.\n'.format(
                    human=human[:-1], scor=scor))
        except SyntaxError:
            registrations_bad.write(
                '{human} \t\t В строке {scor} ошибка SyntaxError. В поле емейл НЕ содержит @ и .(точку): .\n'.format(
                    human=human[:-1], scor=scor))
        except ValueError:
            registrations_bad.write(
                '{human} \t\t В строке {scor} ошибка ValueError. В поле возраст НЕ является числом от 10 до 99.\n'.format(
                    human=human[:-1], scor=scor))
    except IndexError:
        registrations_bad.write('{human} \t\t В строке {scor} ошибка  IndexError. Не присутствуют все 3 поля.\n'.format(
            human=human[:-1], scor=scor))


# Открываем 3 файла: 1 чтение, 2 для записи.
# Далее запускаем функцию для проверки регистрации
scor = 0
with open('registrations.txt', 'r', encoding = 'utf_8') as registrations:
    registrations_bad = open('registrations_bad.log', 'a', encoding = 'utf-8')
    registrations_good = open('registrations_good.log', 'a', encoding = 'utf-8')
    for human in registrations:
        scor += 1
        chek_registrations(human, scor)

    registrations_bad.close()
    registrations_good.close()
