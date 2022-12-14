"""
Задача 3. Во все тяжкие
Что нужно сделать
Фанаты сериала Breaking Bad («Во все тяжкие») написали собственный API по вселенной своего любимого сериала.
Ссылка на документацию: Documentаtion.

Внимательно изучите документацию этого API и напишите программу, которая выводит на экран (а также в JSON-файл)
информацию о том, в каком эпизоде произошло больше всего смертей. Информация хранится в виде словаря, который содержит:

ID эпизода,
номер сезона,
номер эпизода,
общее количество смертей,
список погибших.
"""

import requests
import json

'''
   1. ID эпизода.
   1. Номер сезона.
   1. Номер эпизода.
   1. Общее количество смертей.
   1. Список погибших.
'''

# Проверяем что есть на сайте
films_deaths = requests.get('https://www.breakingbadapi.com/api/')
films_date = json.loads(films_deaths.text)
print(films_date)

# Открываем страницу смертей
deaths_date = requests.get('https://www.breakingbadapi.com/api/deaths/')
deaths = json.loads(deaths_date.text)
# Открываем страницу эпизодов
episodes_date = requests.get('https://www.breakingbadapi.com/api/episodes/')
episodes = json.loads(episodes_date.text)

# Создаем словарь с максимальным количеством смертей
id_deam = dict()
id_deam = max(deaths, key=lambda item: item['number_of_deaths'])

# Выбираем какой словарь подходит по эпизоду и сеансу
result = list(filter(lambda x: x['season'] == str(id_deam['season']) and x['episode'] == str(id_deam['episode']), episodes))

# Создаем словарь с данными фильма
result_deaths = {'ID эпизода': result[0]['episode'], 'Номер сезона': id_deam['season'], 'Номер эпизода': id_deam['episode'],
                 'Общее количество смертей': id_deam['number_of_deaths'], 'Список погибших': id_deam['death']
                 }
# Открываем films.json и записываем в него данные в result_deaths
with open('films.json', 'w', encoding='utf-8') as file:
    json.dump(result_deaths, file, indent=4, ensure_ascii=False)
# Открываем films.json и записываем из него данные в films
with open('films.json', 'r', encoding='utf-8') as file:
    films = json.load(file)
# Выводим на экран
print('='* 40)
for key, value in films.items():
    print(key, value)
print('=' * 40)
print(films)