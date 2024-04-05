import flask
from app import app
import pandas
import sqlite3
from flask import render_template, request, session, redirect, url_for


@app.route('/info', methods=['get'])
def info_user():
    conn = sqlite3.connect("Pet.db")
    cur = conn.cursor()

    if request.values.get('return_equipment'):
        cur.execute(f"""
         INSERT INTO patient_appointment(id_timetable, id_dog) VALUES ('{request.values.get('return_equipment')}', 
          '{request.values.get('dog_id')}')""")
        conn.commit()
        return redirect(url_for('index'))

    list_spec = pandas.read_sql("""
        SELECT id_specialization, name_specialization FROM specialization
        """, conn)

    if request.values.get('name_spec'):
        session['id_specialization'] = int(request.values.get('name_spec'))
    else:
        session['id_specialization'] = 7

    if request.values.get('name_spec'):
        id_spec = request.values.get('name_spec')
    else:
        id_spec = 7

    list_name_users = pandas.read_sql(""" SELECT id_dog_owner, first_name || " " || last_name || " " || surname as FIO
                                                FROM dog_owner """, conn)

    if request.values.get('users'):
        user_selected = request.values.get('users')
    else:
        user_selected=list_name_users['id_dog_owner'].iloc[0]

    list_name_dogs = pandas.read_sql(f""" SELECT id_dog, name_dog
                        FROM dog_owner inner join dog using(id_dog_owner) 
                        where id_dog_owner={user_selected}""", conn)

    dog_id=list_name_dogs['id_dog'].iloc[0]

    list_day = pandas.read_sql(f"""
        SELECT name_dog as Имя, age_dog as Возраст, name_breed_of_dog as Порода
        FROM dog_owner inner join dog using(id_dog_owner) inner join breed_of_dog using(id_breed_of_dog)
        where id_dog_owner == '{user_selected}'
        order by 1
        """, conn)

    list_user_info = pandas.read_sql(f""" SELECT first_name || " " || last_name || " " || surname as FIO, 
                                                    email, phone
                                                    FROM dog_owner 
                                                    where id_dog_owner == '{dog_id}'""", conn)

    return render_template(
        'users_info.html',
        specialization_list=list_spec,
        select_time=list_day,
        users_list=list_name_users,
        dogs_list=list_name_dogs,
        user_id=user_selected,
        dog_id=dog_id,
        FIO_user=list_user_info['FIO'].iloc[0],
        mail_user=list_user_info['email'].iloc[0],
        tel_user=list_user_info['phone'].iloc[0],
        len=len)
