from pony.orm import *

db = Database()


class Teacher(db.Entity):
    id = PrimaryKey(int, auto=True)
    Name = Optional(str, 120)
    teacher__disciplines = Set('Teacher_Discipline')


class Discipline(db.Entity):
    id = PrimaryKey(int, auto=True)
    Name = Optional(str, 140)
    teacher__disciplines = Set('Teacher_Discipline')
    discipline_lessons = Set('Discipline_lesson')


class Teacher_Discipline(db.Entity):
    id_teachers = Required(Teacher)
    id_disciplines = Required(Discipline)
    PrimaryKey(id_teachers, id_disciplines)


class Lesson(db.Entity):
    id = PrimaryKey(int, auto=True)
    discipline_lessons = Set('Discipline_lesson')
    Name = Optional(str, 120)


class Discipline_lesson(db.Entity):
    disciplines = Required(Discipline)
    lessons = Required(Lesson)
    PrimaryKey(disciplines, lessons)


db.generate_mapping()
