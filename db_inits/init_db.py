init_db = '''
    DROP TABLE IF EXISTS day;
    CREATE TABLE day (
        id_day INTEGER PRIMARY KEY,
        name_day TEXT NOT NULL UNIQUE
    );
    
    DROP TABLE IF EXISTS specialization;
    CREATE TABLE specialization (
        id_specialization INTEGER PRIMARY KEY AUTOINCREMENT,
        name_specialization TEXT NOT NULL UNIQUE
    );
    
    DROP TABLE IF EXISTS doctor;
    CREATE TABLE doctor (
        id_doctor INTEGER PRIMARY KEY AUTOINCREMENT,
        id_specialization INTEGER NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        surname TEXT,
        FOREIGN KEY (id_specialization)
            REFERENCES specialization (id_specialization)
              ON DELETE CASCADE
              ON UPDATE NO ACTION
    );
    
    DROP TABLE IF EXISTS work_day;
    CREATE TABLE work_day (
        id_work_day INTEGER PRIMARY KEY AUTOINCREMENT,
        id_doctor INTEGER NOT NULL,
        id_day INTEGER NOT NULL,
        beginning_of_work TEXT NOT NULL,
        end_of_work TEXT NOT NULL,
        work_date TEXT NOT NULL,
        FOREIGN KEY (id_doctor)
           REFERENCES doctor (id_doctor)
              ON DELETE CASCADE
              ON UPDATE NO ACTION,
        FOREIGN KEY (id_day)
           REFERENCES day (id_day)
              ON DELETE CASCADE
              ON UPDATE NO ACTION
    );
    
    DROP TABLE IF EXISTS timetable;
    CREATE TABLE timetable (
        id_timetable INTEGER PRIMARY KEY AUTOINCREMENT,
        id_work_day INTEGER NOT NULL,
        time_work TEXT NOT NULL,
        FOREIGN KEY (id_work_day)
           REFERENCES work_day (id_work_day)
              ON DELETE CASCADE
              ON UPDATE NO ACTION
    );
    
    DROP TABLE IF EXISTS dog_owner;
    CREATE TABLE dog_owner (
        id_dog_owner INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        surname TEXT,
        email TEXT NOT NULL UNIQUE,
        phone TEXT NOT NULL UNIQUE
    );
    
    DROP TABLE IF EXISTS breed_of_dog;
    CREATE TABLE breed_of_dog (
        id_breed_of_dog INTEGER PRIMARY KEY AUTOINCREMENT,
        name_breed_of_dog TEXT NOT NULL UNIQUE
    );
    
    DROP TABLE IF EXISTS dog;
    CREATE TABLE dog (
        id_dog INTEGER PRIMARY KEY AUTOINCREMENT,
        id_dog_owner INTEGER NOT NULL,
        id_breed_of_dog INTEGER NOT NULL,
        name_dog TEXT NOT NULL,
        age_dog TEXT NOT NULL,
        FOREIGN KEY (id_dog_owner)
           REFERENCES dog_owner (id_dog_owner)
              ON DELETE CASCADE
              ON UPDATE NO ACTION,
        FOREIGN KEY (id_breed_of_dog)
           REFERENCES breed_of_dog (id_breed_of_dog)
              ON DELETE CASCADE
              ON UPDATE NO ACTION
    );
    
    DROP TABLE IF EXISTS patient_appointment;
    CREATE TABLE patient_appointment (
        id_patient_appointment INTEGER PRIMARY KEY AUTOINCREMENT,
        id_timetable INTEGER NOT NULL,
        id_dog INTEGER NOT NULL,
        FOREIGN KEY (id_timetable)
           REFERENCES timetable (id_timetable)
              ON DELETE CASCADE
              ON UPDATE NO ACTION,
        FOREIGN KEY (id_dog)
           REFERENCES dog (id_dog)
              ON DELETE CASCADE
              ON UPDATE NO ACTION
    );
'''