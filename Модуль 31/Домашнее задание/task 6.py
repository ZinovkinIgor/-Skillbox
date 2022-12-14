"""
Задача 6. Поиск разницы между двумя JSON-файлами (пример из реального тестового задания на
должность Python-разработчика уровня Junior)
Что нужно сделать
Найдите различия между двумя JSON-файлами. Если различающиеся параметры входят в diff_list,
выведите различие. Иными словами, вам нужно отловить изменение определённых параметров и
вывести значение: что изменилось и на что. Набор ключей в обоих файлах идентичный, различаются лишь значения.

Напишите программу, которая:

загружает данные из двух предложенных JSON-файлов (находятся в репозитории);
выполняет сравнение параметров, указанных в diff_list;
формирует результат в виде словаря;
записывает словарь в JSON-файл с названием result.json.
Исходные данные

Файлы:

json_old.json,
json_new.json.
Список параметров для отслеживания (можно сформировать инпутом или ввести вручную):

diff_list = [‘services’, ‘staff’, ‘datetime’]

Формат итогового словаря с результатом:

Словарь {параметр: новое_значение, ….}

Пример

Данные, загруженные из json_old.json:

{'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create',
'data': {'id': 11111111, 'company_id': 111111, 'services': [{'id': 9035445, 'title': 'Стрижка',
'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [],
'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент',
'phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1,
'datetime': '2022-01-25T11:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00', 'online': False,
'attendance': 0, 'confirmed': 1, 'seance_length': 3600, 'length': 3600, 'master_request': 1,
'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False, 'paid_full': 0,
'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}
Данные, загруженные из json_new.json:

{'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create',
'data': {'id': 11111111, 'company_id': 111111, 'services': [{'id': 22222225, 'title': 'Стрижка',
'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [],
'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент',
'phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1,
'datetime': '2022-01-25T13:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00',
'online': False, 'attendance': 2, 'confirmed': 1, 'seance_length': 3600, 'length': 3600,
'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False,
'paid_full': 1, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}
diff_list = [‘services’, ‘staff’, ‘datetime’]
Результат

print(result)
В консоли должно вывестись следующее сообщение:

{'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
'amount': 1}], 'datetime': '2022-01-25T13:00:00+03:00'}
Помимо вывода в консоль, должен быть сформирован JSON-файл с получившимся словарём (result.json).

Обратите внимание: в result представлены не все изменившиеся поля, а лишь те, что объявлены в diff_list.
"""
import json


old = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create',
'data': {'id': 11111111, 'company_id': 111111, 'services': [{'id': 9035445, 'title': 'Стрижка',
'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [],
'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент',
'phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1,
'datetime': '2022-01-25T11:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00', 'online': False,
'attendance': 0, 'confirmed': 1, 'seance_length': 3600, 'length': 3600, 'master_request': 1,
'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False, 'paid_full': 0,
'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}


new_old = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create',
'data': {'id': 11111111, 'company_id': 111111, 'services': [{'id': 22222225, 'title': 'Стрижка',
'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [],
'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент',
'phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1,
'datetime': '2022-01-25T13:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00',
'online': False, 'attendance': 2, 'confirmed': 1, 'seance_length': 3600, 'length': 3600,
'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False,
'paid_full': 1, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}



with open('json_old.json', 'r') as file:
    text_1 = json.load(file)

with open('json_new.json', 'r') as file:
    text_2 = json.load(file)

print(text_1)
print(text_2)

diff_list = list()
dict_result = dict()


for head in text_1['data']:
    if text_1['data'][head] == text_2['data'][head]:
        pass
    else:
        diff_list.append(head)
        dict_result[f"{head}_1"] = text_1['data'][head]

        dict_result[f"{head}_2"] = text_2['data'][head]


print(diff_list)

for k, v in dict_result.items():
    print("{}: {}".format(k, v))
