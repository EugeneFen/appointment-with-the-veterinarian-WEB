import flask
from app import app
import pandas
import sqlite3
from flask import render_template, request, session, redirect, url_for


@app.route('/', methods=['get', 'post'])
def index():
    conn = sqlite3.connect("Pet.db")
    cur = conn.cursor()

    if request.values.get('return_equipment'):
        cur.execute(f"""
         INSERT INTO patient_appointment(id_timetable, id_dog) VALUES ('{request.values.get('return_equipment')}', 
          '{session['id_dog']}')""")
        conn.commit()
        return redirect(url_for('index'))

    list_spec = pandas.read_sql("""
    SELECT id_specialization, name_specialization FROM specialization
    """, conn)

    if request.values.get('name_spec'):
        session['id_specialization'] = int(request.values.get('name_spec'))
    else:
        session['id_specialization'] = 7

    list_name_users = pandas.read_sql(""" SELECT id_dog_owner, first_name || " " || last_name || " " || surname as FIO
                    FROM dog_owner """, conn)

    if request.values.get('users'):
        session['id_dog_owner'] = int(request.values.get('users'))
    else:
        session['id_dog_owner'] = int(list_name_users['id_dog_owner'].iloc[0])

    list_name_dogs = pandas.read_sql(f""" SELECT id_dog, name_dog
                        FROM dog_owner inner join dog using(id_dog_owner) 
                        where id_dog_owner='{session['id_dog_owner']}'""", conn)

    if request.values.get('dogs'):
        session['id_dog'] = int(request.values.get('dogs'))
    else:
        session['id_dog'] = int(list_name_dogs['id_dog'].iloc[0])

    list_day = pandas.read_sql(f"""
        SELECT work_date as Дата, first_name || " " || last_name || " " || surname as ФИО, time_work as Время, timetable.id_timetable as Запись
        FROM timetable inner join work_day using(id_work_day)
            inner join doctor using(id_doctor)
        where id_specialization = '{session['id_specialization']}' and timetable.id_timetable not in (select id_timetable
                                                                                            from patient_appointment)
        order by 1
        """, conn)

    return render_template(
        'day_list.html',
        specialization_list=list_spec,
        spec_id=session['id_specialization'],
        select_time=list_day,
        users_list=list_name_users,
        dogs_list=list_name_dogs,
        user_id=session['id_dog_owner'],
        dog_id=session['id_dog'],
        len=len)
