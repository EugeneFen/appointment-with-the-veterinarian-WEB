from flask import Flask, session

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import controllers.day_timetable
import controllers.user_appointment
import controllers.view_records
import controllers.user_info_view
import controllers.user_new_insert
import controllers.dog_new_isert