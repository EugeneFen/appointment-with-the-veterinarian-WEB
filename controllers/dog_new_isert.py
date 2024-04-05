import flask
from app import app
import pandas
import sqlite3
from flask import render_template, request, session, redirect, url_for

@app.route('/new_dog', methods=['get', 'post'])
def dog_add():
    conn = sqlite3.connect("Pet.db")
    cur = conn.cursor()

    list_spec = pandas.read_sql("""
    SELECT id_specialization, name_specialization FROM specialization
    """, conn)

    if request.values.get('name_spec'):
        session['id_specialization'] = int(request.values.get('name_spec'))
    else:
        session['id_specialization'] = 7

    list_breed = pandas.read_sql("""
        SELECT id_breed_of_dog, name_breed_of_dog FROM breed_of_dog
        """, conn)

    if request.values.get('breed_dog'):
        session['id_breed_of_dog'] = int(request.values.get('breed_dog'))
    else:
        session['id_breed_of_dog'] = 1

    list_name_users = pandas.read_sql(""" SELECT id_dog_owner, first_name || " " || last_name || " " || surname as FIO
                        FROM dog_owner """, conn)

    if request.values.get('insert_dog'):
        if request.values.get('user_name') and request.values.get('dog_age') and request.values.get('users') \
                and request.values.get('breed_dog'):
            cur.execute(f"""INSERT INTO dog(id_dog_owner, id_breed_of_dog, name_dog, age_dog) VALUES
                            ('{request.values.get('users')}', '{request.values.get('breed_dog')}', '{request.values.get('user_name')}',
                            '{request.values.get('dog_age')}')""")
            conn.commit()
            return render_template(
                'new_dog.html',
                specialization_list=list_spec,
                spec_id=session['id_specialization'],
                users_list=list_name_users,
                user_id=1,
                us_name=request.values.get('user_name'),
                breed_of_dog_list=list_breed,
                breed_id={request.values.get('breed_dog')},
                us_last=request.values.get('dog_age'),
                output_results="Добавлен",
                len=len)

    return render_template(
        'new_dog.html',
        specialization_list=list_spec,
        spec_id=session['id_specialization'],
        users_list=list_name_users,
        user_id=1,
        breed_of_dog_list=list_breed,
        breed_id=session['id_breed_of_dog'],
        us_name="",
        us_last="",
        output_results="Не добавлен",
        len=len)