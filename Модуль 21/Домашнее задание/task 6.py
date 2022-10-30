"""
Задача 6. Глубокое копирование
Что нужно сделать
Вы сделали для заказчика структуру сайта по продаже телефонов:

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': ‘Продать'
        }
    }
}
Заказчик рассказал своим коллегам на рынке, и они тоже захотели такой сайт, только для своих товаров.
Вы посчитали, что это лёгкая задача, и быстро принялись за работу.
Напишите программу, которая запрашивает у клиента, сколько будет сайтов, а затем запрашивает название продукта и
после каждого запроса выводит на экран активные сайты.
Условия: структуру сайта нужно описать один раз, копипасту никто не любит.
Подсказка: используйте рекурсию.

Пример:
Сколько сайтов: 2
Введите название продукта для нового сайта: iPhone
Сайт для iPhone:

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам iPhone недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': ‘Продать'
        }
    }
}

Введите название продукта для нового сайта: Samsung

Сайт для iPhone:

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам iPhone недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': ‘Продать'
        }
    }
}

Сайт для Samsung:
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам Samsung недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на Samsung',
            'div': 'Купить',
            'p': ‘Продать'
        }
    }
}
"""
import copy

def print_site(new_site, scor=0):
    for i_name, i_volum in new_site.items():
        if isinstance(i_volum, dict):
            scor += 1
            print(i_name)
            print_site(i_volum)
        else:
            print('\t', i_name, ':', i_volum)

def new_site(site, score):
    for _ in range(score):
        new_dict_site.clear()
        name = input('Введите название продукта для нового сайта: ')
        site['html']['head']['title'] = ['Куплю/продам {} недорого'.format(name)]
        site['html']['body']['h2'] = ['У нас самая низкая цена на {}'.format(name)]
        site['html']['body']['div'] = ['Купить']
        site['html']['body']['p'] = ['Продать']
        dict_site['Сайт для магазина {}'.format(name)] = copy.deepcopy(site)
        print_site(dict_site)
    return dict_site


dict_site = dict()
new_dict_site = dict()
name = None
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {} недорого'.format(name)
        },
        'body': {
            'h2': 'У нас самая низкая цена на {}'.format(name),
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

score = int(input('Введите количество сайтов: '))
result = new_site(site, score)
