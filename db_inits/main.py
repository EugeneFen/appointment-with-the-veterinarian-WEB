import sqlite3
import pandas as pd
from fill_db import *
from init_db import *

connect = sqlite3.connect("../Pet.db")
cursor = connect.cursor()
# # * init db
# cursor.executescript(init_db)
#
# # * fill db
# cursor.executescript(fill_script)

# cursor.execute("""
# SELECT work_date as Дата, first_name || " " || last_name || " " || surname as ФИО, name_specialization as Специализация, time_work as Время
#             FROM patient_appointment inner join timetable using(id_timetable) inner join work_day using(id_work_day)
#                 inner join doctor using(id_doctor) inner join specialization using(id_specialization)
#             where patient_appointment.id_dog == '1'
#             order by 1
# """)
# print(cursor.fetchall())
#
# cursor.execute("""
# delete from patient_appointment where id_dog == "None"
# """)
# print(cursor.fetchall())
#
# cursor.execute("""
# select * FROM patient_appointment
# """)
# print(cursor.fetchall())

cursor.execute("""
select * FROM dog
""")
print(cursor.fetchall())

cursor.execute("""
update dog_owner
set surname = "Отсутствует"
where surname is Null
""")
cursor.execute("""
select * FROM dog_owner
""")
print(cursor.fetchall())

connect.commit()
connect.close()