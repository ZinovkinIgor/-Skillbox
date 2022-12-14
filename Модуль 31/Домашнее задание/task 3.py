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
import random
import random
import requests
import json

url = 'https://www.breakingbadapi.com/api/'
url_characters = 'https://www.breakingbadapi.com/api/characters/'
url_episodes = 'https://breakingbadapi.com/api/episodes'
url_quotes = 'https://breakingbadapi.com/api/quotes'
url_deaths = 'https://breakingbadapi.com/api/deaths'

site = requests.get(url)
print(site.text)
#
# site_ch = requests.get(url_characters)
# print(site_ch)
# #
# site_ep = requests.get(url_episodes)
# site = json.loads(site_ep.text)
#
# site_de = requests.get(url_deaths)
# print(site_de.text)
#
# site_qu = requests.get(url_quotes)
# print(site_qu.text)

#
# with open('episodes.json', 'w') as episod:
#     json.dump(site, episod, indent=4)