"""
Задача 2. Студенты
Что нужно сделать
Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
Затем создайте список из десяти студентов (данные о студентах можете придумать свои или запросить их у пользователя)
и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.
"""

class Student:

    def __init__(self, human):
        self.surname = human[0]
        self.name = human[1]
        self.group = human[2]
        self.grade = human[3:]
        self.evaluations(self.grade)

    def evaluations(self, grade_student, summ=0, count=0):
        for numb in grade_student:
            count += 1
            summ += int(numb)
            self.result_grade = round(summ / count, 2)


class Journal:

    def __init__(self, scor):
        self.scor = scor
        self.human()

    def human(self):
        for _ in range(self.scor):
            human = input('Введите через пробел (фамилию, Имя, Номер учебной группы, оценки): ').split()
            record = Student(human)
            student_dict[record.surname, record.name, record.group] = record.result_grade

        for name in sorted(student_dict.items(), key=lambda x: x[1], reverse=True):
            print('{} средний бал: {}'.format(
                ' '.join(name[0]),
                name[1]))

student_dict =dict()
user = Journal(5)
