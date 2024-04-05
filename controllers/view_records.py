import flask
from app import app
import pandas
import sqlite3
from flask import render_template, request, session, redirect, url_for


@app.route('/view', methods=['get'])
def view():
    conn = sqlite3.connect("Pet.db")
    cur = conn.cursor()

    list_spec = pandas.read_sql("""
        SELECT id_specialization, name_specialization FROM specialization
        """, conn)

    if request.values.get('name_spec'):
        session['id_specialization'] = int(request.values.get('name_spec'))
    else:
        session['id_specialization'] = 7

    cur.execute(f"""
        SELECT first_name || " " || last_name || " " || surname FROM dog_owner
        where id_dog_owner = '{session['id_dog_owner']}'""")

    user_selected = cur.fetchall()

    cur.execute(f"""
            SELECT name_dog FROM dog 
            where id_dog = '{session['id_dog']}'""")

    dog_name = cur.fetchall()

    list_day = pandas.read_sql(f"""
            SELECT work_date as Дата, first_name || " " || last_name || " " || surname as ФИО, name_specialization as Специализация, time_work as Время
            FROM patient_appointment inner join timetable using(id_timetable) inner join work_day using(id_work_day)
                inner join doctor using(id_doctor) inner join specialization using(id_specialization)
            where patient_appointment.id_dog == '{session['id_dog']}'
            order by 1
            """, conn)

    return render_template(
        'view_records_dog.html',
        select_time=list_day,
        user_name=user_selected[0][0],
        dog_name=dog_name[0][0],
        len=len)