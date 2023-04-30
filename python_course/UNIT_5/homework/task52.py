#todo:
#  Разработать систему учета решения задач учениками курса «Разработчик на Питоне».
#
# Проблема.
# Преподаватель каждый урок задает некоторое количество задач в качестве домашнего задания, для упрощения можно считать, что одну.
# Каждый ученик решает каждую задачу. Переводит ее статус в решенную.
# Преподаватель проверяет каждую задачу каждого ученика и либо подтверждает ее статус как решенную или меняет ее статус как не решенную.
# Вопрос. Как спроектировать систему классов на Питоне для решения задачи учета?
# Разработайте систему
# классов (Teacher, Pupil, Lesson, Task. Нужен ли класс Группа?);
# атрибутов для каждого состояния каждого объекта;
# методов для каждого объекта.
# Отчетность? Запросы? Начните с формулировки решаемой задачи – спецификации или технического задания. Затем спроектируйте классы, атрибуты, методы. Протестируйте систему.
'''
Система должна позволять преподавателю задавать ученикам задачи в качестве домашнего задания, ученики должны иметь возможность решать эти задачи и переводить их статус в решенные, а преподаватель должен проверять решения учеников и подтверждать их статус как решенные или менять их статус на не решенные.

Классы:

Teacher - класс для представления преподавателя.
Pupil - класс для представления ученика.
Lesson - класс для представления урока.
Task - класс для представления задачи.

Атрибуты:

Teacher:
- name - имя преподавателя
- lessons - список уроков, проведенных преподавателем

Pupil:
- name - имя ученика
- tasks - список задач, назначенных ученику

Lesson:
- teacher - экземпляр класса Teacher, преподаватель урока
- pupils - список экземпляров класса Pupil, ученики на уроке
- tasks - список экземпляров класса Task, задачи на уроке

Task:
- name - название задачи
- is_solved - статус решения задачи (True/False)
- pupil - экземпляр класса Pupil, ученик, которому назначена задача
'''


class Teacher:
    def __init__(self, name):
        self.name = name

    def check_task(self, task, pupil):
        pupil.task_status[task] = "checked"


class Pupil:
    def __init__(self, name):
        self.name = name
        self.task_status = {}

    def solve_task(self, task):
        self.task_status[task] = "solved"


class Lesson:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.pupils = []

    def add_task(self, task):
        self.tasks.append(task)

    def add_pupil(self, pupil):
        self.pupils.append(pupil)


class Task:
    def __init__(self, name):
        self.name = name


# Пример использования классов:

teacher1 = Teacher('Виталий')
pupil1 = Pupil("Артем")
pupil2 = Pupil("Иван")
lesson1 = Lesson("урок1")
task1 = Task("задача1")
task2 = Task("задача2")

lesson1.add_task(task1)
lesson1.add_task(task2)
lesson1.add_pupil(pupil1)
lesson1.add_pupil(pupil2)

teacher1.check_task(task1, pupil1)
pupil2.solve_task(task2)

print("Lesson %s has %d tasks and %d pupils." % (lesson1.name, len(lesson1.tasks), len(lesson1.pupils)))
print("Pupil %s has solved task %s: %s" % (pupil1.name, task1.name, pupil1.task_status[task1]))
print("Pupil %s has solved task %s: %s" % (pupil2.name, task2.name, pupil2.task_status[task2]))
