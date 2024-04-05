import flask
from app import app
import pandas
import sqlite3
from flask import render_template, request, session, redirect, url_for

@app.route('/new', methods=['get', 'post'])
def user_add():
    conn = sqlite3.connect("Pet.db")
    cur = conn.cursor()

    list_spec = pandas.read_sql("""
    SELECT id_specialization, name_specialization FROM specialization
    """, conn)

    if request.values.get('name_spec'):
        session['id_specialization'] = int(request.values.get('name_spec'))
    else:
        session['id_specialization'] = 7

    if request.values.get('insert_user'):
        if request.values.get('user_name') and request.values.get('user_last_name') and \
                request.values.get('user_mail') and request.values.get('user_phone'):
            if request.values.get('user_surname'):
                cur.execute(f"""INSERT INTO dog_owner(first_name, last_name, surname, email, phone) VALUES
                ('{request.values.get('user_name')}', '{request.values.get('user_last_name')}', '{request.values.get('user_surname')}',
                '{request.values.get('user_mail')}', '{request.values.get('user_phone')}')""")
                conn.commit()
                return render_template(
                    'new_user.html',
                    specialization_list=list_spec,
                    spec_id=session['id_specialization'],
                    us_name=request.values.get('user_name'),
                    us_last=request.values.get('user_last_name'),
                    us_sur=request.values.get('user_surname'),
                    us_mail=request.values.get('user_mail'),
                    us_phon=request.values.get('user_phone'),
                    output_results="Добавлен",
                    len=len)
            else:
                cur.execute(f"""INSERT INTO dog_owner(first_name, last_name, surname, email, phone) VALUES
                        ('{request.values.get('user_name')}', '{request.values.get('user_last_name')}', "Отсутствует",
                        '{request.values.get('user_mail')}', '{request.values.get('user_phone')}')""")
                conn.commit()
                return render_template(
                    'new_user.html',
                    specialization_list=list_spec,
                    spec_id=session['id_specialization'],
                    us_name=request.values.get('user_name'),
                    us_last=request.values.get('user_last_name'),
                    us_sur="",
                    us_mail=request.values.get('user_mail'),
                    us_phon=request.values.get('user_phone'),
                    output_results="Добавлен",
                    len=len)

    return render_template(
        'new_user.html',
        specialization_list=list_spec,
        spec_id=session['id_specialization'],
        us_name="",
        us_last="",
        us_sur="",
        us_mail="",
        us_phon="",
        output_results="Не добавлен",
        len=len)