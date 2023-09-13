import sqlite3


conn = sqlite3.connect("Learn_More_University.db")

try:

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   studentID VARCHAR(15) NOT NULL, 
                   first_name VARCHAR(20) NOT NULL, 
                   last_name VARCHAR(20) NOT NULL, 
                   age INTEGER NOT NULL, 
                   gender CHAR(6) NOT NULL, 
                   course VARCHAR(80) NOT NULL
                   )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   employeeID VARCHAR(15) NOT NULL,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   age INTEGER NOT NULL,
                   gender CHAR(6) NOT NULL,
                   salary INTEGER NOT NULL,
                   department VARCHAR(80) NOT NULL,
                   designation VARCHAR(50) NOT NULL
                   )''')

    conn.commit()

    print("Student and Employee tables created successfully")


except sqlite3.Error as e:
    print("SQLite error:", e)
    conn.rollback()

finally:
    conn.close()
