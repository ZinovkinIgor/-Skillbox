"""
Задача 10. Почта
Что нужно сделать

Почтовое отделение открывается в 08:00 и закрывается в 22:00. С 14:00 до 15:00 все сотрудники уходят на обед,
а в 10:00 и 18:00 приезжают машины с посылками, и тогда все сотрудники на два часа заняты их разгрузкой.
Во время обеда, разумеется, посылки никто не выдаёт, как и в моменты, когда разгружаются машины.
Напишите программу, которая получает на вход время в часах — число от 0 до 23 — и пишет,
можно ли в этот час получить посылку. Используйте только один условный оператор if-else, без elif и прочего.
Решите задание двумя способами:
При выполнении условия выводится сообщение: «Можно получить посылку».
При выполнении условия выводится сообщение: «Посылку получить нельзя».

Советы и рекомендации
Обратите внимание на количество условий и постарайтесь сократить их. Не используйте перечисление конкретных
часов вида a == 1 and a == 2...
"""

time = int(input('Введите время получения посылки: '))
if time >= 8 and time < 10 or time >= 12 and time < 14 or time >= 15 and time < 18 or time >= 20 and time < 22:
    print('Можно получить посылку')
else:
    print('Посылку получить нельзя')