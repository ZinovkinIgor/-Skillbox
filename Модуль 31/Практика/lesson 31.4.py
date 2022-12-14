"""
Задача 1. Звёздные войны
Повторите пример парсинга, разобранный в уроке: перейдите на сайт с API, посвящённый вселенной Star Wars.

После этого сгенерируйте реквест-ссылку на данные о человеке под номером 3 (people/3/).

Затем напишите программу, которая парсит данные об этом человеке, изменяет его имя на ваше
собственное и сохраняет результат в виде JSON-файла.

Дополнительно: обратите внимание на значение ключа homeworld — там также хранится ссылка.
В том же коде спарсите эту ссылку и посмотрите, что там.

Примечание: API тоже пишут люди, а значит, время от времени его могут как-то менять и
усовершенствовать, поэтому будьте внимательны: может быть, ссылка уже хранится в другом ключе.


Задача 2. Документация API
Обычно к открытым API прилагается подробная документация, где описывается логика формирования
ссылок и какие данные по ним можно получать (или отправлять!).

Изучите документацию того же сайта по «Звёздным войнам».

Поэкспериментируйте с получением данных о кораблях, планетах, фильмах и так далее.
А ещё попробуйте библиотеку swapi (о ней также в документации) и с её помощью выведите
начало сюжета из фильма «Новая надежда» (A New Hope).
"""
import requests
import json

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))
if task == 1:
    # Задача 1
    print('=' * 40)

    site = requests.get('https://swapi.dev/api/people/3/')
    text = json.loads(site.text)
    new_site = text['homeworld']
    text['name'] = 'IGOR'

    with open('people.json', 'w', encoding='utf-8') as file:
        json.dump(text, file, indent=4)


    new_text = requests.get(new_site)
    text_2 = json.loads(new_text.text)
    print(text_2)

    with open('new_people.json', 'w') as file:
        json.dump(text_2, file, indent=4)



elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    result = requests.get("https://swapi.dev/api/films/1/")

    json_dict = json.loads(result.text)

    with open('films.json', 'w') as film:
        json.dump(json_dict, film, indent=4)

    print(json_dict["opening_crawl"])

elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

    site = requests.get('https://swapi.dev/api/planets/3/')
    text = json.loads(site.text)
    print(text)
    with open('test.json', 'w', encoding='utf-8') as file:
        json.dump(text, file, indent=4)

else:
    print('Выберите задачу заново.')