"""
Задача 10. Шифр Цезаря
Что нужно сделать
Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась на следующую по алфавиту через K
позиций по кругу. Если взять русский алфавит и K = 3, то в слове, которое мы хотим зашифровать, буква А станет
буквой Г, Б станет Д и так далее.
Пользователь вводит сообщение, а также значение сдвига. Напишите программу, которая зашифрует это сообщение при
помощи шифра Цезаря.

Пример:
Введите сообщение: это питон.
Введите сдвиг: 3
Зашифрованное сообщение: ахс тлхср.
"""

alphabet ='абвгдежзийклмнопрстуфхцчшщъыьэюя'

message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
new_message = []

for simbil in message[:]:
    scor = 0
    for letter in alphabet:
        scor += 1
        if simbil == letter:
            new_message.append(alphabet[(scor + shift - 1) % len(alphabet)])
        elif simbil == ' ':
            new_message.append(' ')
            break
        elif simbil == '.':
            new_message.append('.')
            break
print('Зашифрованное сообщение: ', end=' ')
for simb in new_message:
    print(simb, end='')


print('\n\n', '=' * 20, 'Или', '=' * 20, '\n\n')


alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
    'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
    'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
    'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
    ]
new_str = ' '
text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

# делаем сдвиг букв
new_text = [
            (alphabet[(alphabet.index(x) + shift) % 33]
            if x in alphabet else x)
            for x in text
            ]
for text_str in new_text:
    new_str += text_str
print('Зашифрованное сообщение: ', new_str)



