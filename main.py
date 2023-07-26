import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Arghay@1234@",
    database = "school"
)

query = "CREATE DATABASE IF NOT EXISTS school"
cursor = connection.cursor()

cursor.execute(query)

def create_table(tablename):
    query = f"""
                CREATE TABLE IF NOT EXISTS {tablename}(
                    id INT PIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    age INT,
                    grade FLOAT
                )
            """
    # cursor = connection.cursor()
    # cursor.execute(query)

def add_student(name, age, grade):
    query = """
                INSERT INTO students(name, age, grade)
                VALUES(%s, %s, %s)
            """
    cursor = connection.cursor()
    cursor.execute(query, (name, age, grade))

    connection.commit()

def update_grade(id, grade):
    query = """
                UPDATE students
                SET grade = %s
                WHERE id = %s
            """
    cursor = connection.cursor()
    cursor.execute(query, (id, grade))

def increase_age(id, value):
    query = """
                Select age FROM students WHERE id = %s
            """
    cursor = connection.cursor()
    cursor.execute(query, (id))

    age = cursor.fetchone()
    newage = age[0] + value
    cursor.execute("""
                        UPDATE student 
                        SET age = %s
                        WHERE id = %s
                   """, (newage,id))
    connection.commit()
    

def view_all_student():
    query = " SELECT * FROM students"
    cursor = connection.cursor()
    cursor.execute(query)
    students = cursor.fetchall()
    
    for student in students:
        print(f"""
                id = {student[0]}
                name = {student[1]}
                age = {student[2]}
                grade = {student[3]}
              """)



while  True:
    print("""
            1. Create Table
            2. Add Student
            3. Update Grade
            4. Increase Age
            5. View All Student
            0. Exit
          """)
    option = int(input("Enter your Option: "))

    if(option == 1):
        tablename = input("Enter Tablename: ")
        create_table(tablename)
    elif(option == 2):
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        grade = float(input("Enter Grade: "))
        add_student(name, age, grade)
    elif(option == 3):
        id = int(input("Enter id: "))
        grade = float(input("Enter New Grade: "))
        update_grade(id, grade)
    elif(option == 4):
        id = int(input("Enter id: "))
        value = int(input("Enter number of age want to increase: "))
        increase_age(id, value)
    elif(option == 5):
        view_all_student()
    elif(option == 0):
        break
    else:
        print("Wrong Option selected")

