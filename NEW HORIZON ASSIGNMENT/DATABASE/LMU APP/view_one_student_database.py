import sqlite3


conn = sqlite3.connect("Learn_More_University.db")

try:
    var1 = input("Enter Student ID: ")

    cursor = conn.cursor()

    viewstudentquery = "SELECT studentID, first_name, last_name, age, gender, course FROM Students WHERE studentID ='" + var1 + "' "

    result = cursor.execute(viewstudentquery)
    conn.commit()

    for i in result:
        print(f"Student ID: {i[0]}\nFirst Name: {i[1]}\nLast Name: {i[2]}\nAge: {i[3]}\nGender: {i[4]}\nCourse: {i[5]}\n\n")

except sqlite3.Error as e:
    print("SQLite error:", e)
    conn.rollback()

finally:
    conn.close()
