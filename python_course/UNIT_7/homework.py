import psycopg2
from psycopg2 import Error

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="Python2023")


    cursor = connection.cursor()

    # 1. Выдавать сводную информацию обо всех работниках кафедры;
    cursor.execute("select * from teacher t ;")
    record = cursor.fetchall()
    print("Результат", record)

    # 2. Выдавать информацию о НИР;
    cursor.execute("select name \
                     from discipline d \
                    where 'name'like '%НИР%'; ")
    record = cursor.fetchall()
    print("Результат", record)

    # 3. Выдавать информацию о преподавателе, ведущего указанный вид занятий
    # по указанной дисциплине;
    cursor.execute('''select t."name" 
                    from lesson l 
                    left join discipline_lesson dl on l.id =dl.lessons 
                    left join discipline d on d.id = dl.disciplines 
                    left join teacher_discipline td on td.id_disciplines = d.id 
                    left join teacher t on t.id = td.id_teachers 
                    where l."name" ='lesson_1';''')
    record = cursor.fetchall()
    print("Результат", record)

    # 4. Выдавать информацию о видах занятий, которые проводятся по
    # выбранной дисциплине.
    cursor.execute('''select l."name" 
                    from discipline d 
                    left join discipline_lesson dl on dl.disciplines = d.id 
                    left join lesson l on l.id = dl.lessons 
                    where d."name" = 'Предмет_2';''')
    record = cursor.fetchall()
    print("Результат", record)



except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
