import mysql.connector
import bcrypt


db = mysql.connector.connect(
    host="localhost",
    user="akash",
    password="akash",
    database="userdb"
)

cursor = db.cursor()

def signup():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, hashed_password)

    try:
        cursor.execute(sql, values)
        db.commit()
        print("Signup successful!")
    except:
        print("Email already exists!")





while True:
        print("\n========= Student Page =========")
        print("1. SignUp")
       
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            signup()
           

        
        elif choice == "2":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")
