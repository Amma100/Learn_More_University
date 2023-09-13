import sqlite3


conn = sqlite3.connect("Learn_More_University.db")

try:
    var1 = input("Enter Employee ID: ")

    cursor = conn.cursor()

    viewemployeequery = "SELECT employeeID, first_name, last_name, age, gender, salary, department, designation FROM Employee WHERE employeeID ='" + var1 + "' "

    result = cursor.execute(viewemployeequery)
    conn.commit()

    for i in result:
        print(f"Employee ID: {i[0]}\nFirst Name: {i[1]}\nLast Name: {i[2]}\nAge: {i[3]}\nGender: {i[4]}\nSalary: {i[5]}\nDepartment: {i[6]}\nDesignation: {i[7]}\n\n")

except sqlite3.Error as e:
    print("SQLite error:", e)
    conn.rollback()

finally:
    conn.close()
