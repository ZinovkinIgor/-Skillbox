"""
Задача 3. Дата
Что нужно сделать
Реализуйте класс Date, который должен:

проверять числа даты на корректность;
конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.

При тестировании программы объект класса Date должен инициализироваться исключительно через метод конвертации, например:

date = Date.from_string('10-12-2077')
Неверный вариант: date = Date(10, 12, 2077)

Пример основного кода:

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

Результат:
День: 10    Месяц: 12    Год: 2077
True
False
"""


class Date:
    '''
    more - месяца в которых 31 день
    less - месяца в которых 30 дней
    '''
    more = [1, 3, 5, 7, 8, 10, 12]
    less = [4, 6, 9, 11]

    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        """
        выводим на экран дату
        :return: дату
        """
        return 'День: {day}	Месяц: {month}	Год: {year}'.format(
            day=self.day, month=self.month, year=self.year)

    @classmethod
    def checking_date(cls, day: int, month: int, year: int) -> bool:
        """
        проверяет на актуальность даты, если такой даты нет то выходит ошибка
        """
        try:
            if month in Date.more:
                '''Если месяц есть в списке месяцев с 31 днем.'''
                if day <= 31:
                    return True
                else:
                    raise Exception('Ошибка дня.')

            elif month in Date.less:
                '''Если месяц есть в списке месяцев с 30 днями.'''
                if day <= 30:
                    return True
                else:
                    raise Exception('Ошибка дня.')

            elif month == 2:
                '''Если месяц февраль'''
                if year % 4 == 0:
                    """Проверяем год, является ли он высокосным то 29 дней иначе 28"""
                    if day <= 29:
                        return True
                    else:
                        raise Exception('Ошибка дня.')
                else:
                    if day <= 28:
                        return True
                    else:
                        raise Exception('Ошибка дня.')
            else:
                raise Exception('Ошибка месяца.')
        except Exception:
            print('Введите другую дату')


    @classmethod
    def from_string(cls, date: str) -> list:
        """ делим строку отправляем на проверку дату и после проверки возвращаем"""
        int_date = date.split('-')
        day, month, year = int(int_date[0]), int(int_date[1]), int(int_date[2])
        if cls.checking_date(day, month, year) == True:
            date_out = cls(day, month, year)
            return date_out

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        int_date = date.split('-')
        day, month, year = int(int_date[0]), int(int_date[1]), int(int_date[2])
        if cls.checking_date(day, month, year) == True:
            return True
        else:
            return False



date = Date.from_string('28-02-2001')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))






