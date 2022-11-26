"""
Задача 4. Компания
Что нужно сделать

Реализуйте иерархию классов, описывающих служащих в компании. На самом верху иерархии — класс Person,
который описывает человека именем, фамилией и возрастом. Все атрибуты этого класса являются приватными.
Далее идёт класс Employee и производные от него классы Manager, Agent и Worker.
Класс «Работник» должен иметь метод расчёта заработной платы, переопределённый в каждом из производных классов.
Заработная плата Manager постоянна и равна 13000, заработная плата Agent определяется как оклад 5000 + 5% от
объёма продаж, который хранится в специальном поле класса Agent, а заработная плата Worker определяется как
100 * число отработанных часов, которое также хранится в отдельном поле.
В основной программе создайте список из девяти объектов: первые три — Manager, следующие три — Agent и последние
три — Worker. Выведите на экран величину заработной платы всех девяти служащих
"""


class Person:
    """
    Класс Person
    args:
        __name - имя
        __surname - фамилия
        __age - возраст
    """

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        """Возвращает имя"""
        return self.__name

    def get_surname(self):
        """Возвращает фамилию"""
        return self.__surname

    def get_age(self):
        """Возвращает возраст"""
        return self.__age


class Employee(Person):
    # def __init__(self, name, surname, age):
    #     super().__init__(name, surname, age)

    def salary_emp(self):
        return 13000

    def emp_info(self):
        print('Имя: {name}\nФамилия: {surname}\nВозраст: {age}\nЗарплата: {salary}\n'.format(
            name=self.get_name(),
            surname=self.get_surname(),
            age=self.get_age(),
            salary=self.salary_emp()))


class Manager(Employee):
    """
    Зарплата менеджера постоянная и ровна 13к
    """
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

class Agent(Employee):
    """
    Зарплата агента равна 5000 + 5% от объема продаж
    """
    def __init__(self, name, surname, age, volum_sales):
        super().__init__(name, surname, age)
        self.volum_sales = volum_sales

    def salary_emp(self):
        salary = 5000 + self.volum_sales * 5 / 100
        return salary
class Worker(Employee):
    """
    Зарплата работника равна 100р час
    """
    def __init__(self, name, surname, age, hoer):
        super().__init__(name, surname, age)
        self.hoer = hoer

    def salary_emp(self):
        salary = 100 * self.hoer
        return salary

list_employee = [['Игорь', 'Зиновкин', 34],
                 ['Иван', 'Петров', 39],
                 ['Ольга', 'Филиппова', 25],
                 ['Никита', 'Федотов', 45, 1000000],
                 ['Глеб', 'Игогот', 30, 700000],
                 ['Юля', 'Нестерова', 41, 900000],
                 ['Толик', 'Болиг', 38, 200],
                 ['Вика', 'Фопина', 35, 160],
                 ['Настя', 'Гришина', 19, 130]
                 ]
scor = 0
summ_salary = 0
for res in list_employee:
    scor += 1
    if scor <= 3:
        human = Manager(name=res[0], surname=res[1], age=res[2])
        human.emp_info()
        summ_salary += human.salary_emp()
    elif scor <= 6:
        human = Agent(name=res[0], surname=res[1], age=res[2], volum_sales=res[3])
        human.emp_info()
        summ_salary += human.salary_emp()
    elif scor <= 9:
        human = Worker(name=res[0], surname=res[1], age=res[2], hoer=res[3])
        human.emp_info()
        summ_salary += human.salary_emp()
print('Сумма всех зарплат: {} рублей'.format(summ_salary))

