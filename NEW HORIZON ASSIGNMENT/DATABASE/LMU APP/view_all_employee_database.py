import sqlite3


conn = sqlite3.connect("Learn_More_University.db")

try:

    cursor = conn.cursor()

    viewemployeequery = "SELECT * FROM Employee"

    result = cursor.execute(viewemployeequery)
    conn.commit()

    for i in result:
        print(f"ID: {i[0]}\nEmployee ID: {i[1]}\nFirst Name: {i[2]}\nLast Name: {i[3]}\nAge: {i[4]}\nGender: {i[5]}\nSalary: {i[6]}\nDepartment: {i[7]}\nDesignation: {i[8]}\n\n")

except sqlite3.Error as e:
    print("SQLite error:", e)
    conn.rollback()

finally:
    conn.close()
