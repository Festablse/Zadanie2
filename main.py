print("------------------------------------------------------")
print("Часть8 №1-2")
import sqlite3
conn = sqlite3.connect('db1.sqlite')
cursor = conn.cursor()
cursor.execute("CREATE TABLE Students (id int, name Varchar(32), surname Varchar (32), age int, city Varchar (32))") cursor.execute("CREATE TABLE Courses (id int, name Varchar(32), time_start Varchar(32), time_end Varchar(32))") 
cursor.execute("CREATE TABLE Students_courses (student_id int, course_id int)") cursor.execute('''INSERT INTO Courses (id,name,time_start,time_end) VALUES (1,'python','21.07.21','21.08.21')''') cursor.execute('''INSERT
INTO Courses (id,name,time_start,time_end) VALUES (2,'java','13.07.21','16.08.21')''') cursor.execute('''INSERT INTO Students (id,name,surname,age,city) VALUES (1,'Max','Brooks',24,'Spb')''') cursor.executemany('INSERT INTO
Students VALUES(?,?,?,?,?)',[(2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'),(4, 'Kate', 'Brooks', 34, 'Spb')]) cursor.executemany('INSERT INTO Students_courses VALUES(?,?)', [(1, 1), (2, 1), (3, 1), (4,2)])
cursor.execute('SELECT Students.name, Students.surname FROM Students WHERE age > 30')
print("Все студенты старше 30 лет:", cursor.fetchall())
cursor.execute('SELECT Students.name, Students.surname FROM Students_courses JOIN Students ON '
               'Students_courses.student_id = Students.id WHERE course_id = 1')
print("Все студенты, которые проходят курс по python:", cursor.fetchall())
cursor.execute('SELECT Students.name, Students.surname FROM Students_courses JOIN Students ON '
               'Students_courses.student_id = Students.id WHERE course_id = 1 AND Students.city = "Spb"')
print("Все студенты, которые проходят курс по python и из СПб:", cursor.fetchall())
#conn.commit()
conn.close()
print("------------------------------------------------------")
print("Часть8 №3")
#(from peewee import *
conn = SqliteDatabase('db2.sqlite')
class Students(Model):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')
    class Meta:
        database = conn
class Courses(Model):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    time_start = CharField(column_name='time_start')
    time_end = CharField(column_name='time_end')
    class Meta:
        database = conn
class Students_courses(Model):
    student_id = ForeignKeyField(Students, to_field='id', column_name='students_id')
    course_id = ForeignKeyField(Courses, to_field='id', column_name='course_id')
    class Meta:
        database = conn
Students.create_table()
Courses.create_table()
Students_courses.create_table()
s1 = [{'id': 1, 'name': 'Max', 'surname': 'Brooks', 'age': 24, 'city': 'Spb'},
      {'id': 2, 'name': 'John', 'surname': 'Stones', 'age': 15, 'city': 'Spb'},
      {'id': 3, 'name': 'Andy', 'surname': 'Wings', 'age': 45, 'city': 'Manhester'},
      {'id': 4, 'name': 'Kate', 'surname': 'Brooks', 'age': 34, 'city': 'Spb'}]
Students.insert_many(s1).execute()
c1 = [{'id': 1, 'name': 'python', 'time_start': '21.07.21', 'time_end': '21.08.21'},
      {'id': 2, 'name': 'java', 'time_start': '13.07.21', 'time_end': '16.08.21'}]
Courses.insert_many(c1).execute()
s_c1 = [{'student_id': 1, 'course_id': 1},
        {'student_id': 2, 'course_id': 1},
        {'student_id': 3, 'course_id': 1},
        {'student_id': 4, 'course_id': 2}]
Students_courses.insert_many(s_c1).execute()
students_over30 = Students.select().where(Students.age > 30)
for i in students_over30:
    print('Cтудент старше 30 лет:', i.name, i.surname)
students_python = Students.select().join(Students_courses).where(Students_courses.course_id == 1)
for r in students_python:
    print('Cтудент, который проходит курс по python:', r.name, r.surname)
students_spb = Students.select().join(Students_courses).where(
    Students_courses.course_id == 1, Students.city == 'Spb')
for k in students_spb:
    print('Cтудент, который проходит курс по python и из СПб:', k.name, k.surname))
print("------------------------------------------------------")
