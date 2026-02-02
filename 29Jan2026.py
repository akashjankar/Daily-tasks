from flask import Flask, request, jsonify
import mysql.connector
import bcrypt

app = Flask(__name__)


db = mysql.connector.connect(
    host="localhost",
    user="akash",
    password="akash",
    database="userdb"
)

cursor = db.cursor(dictionary=True)




@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to User API by Akash</h1>"




@app.route("/signup", methods=["POST"])
def signup():
    data = request.json

    if not data or "name" not in data or "email" not in data or "password" not in data:
        return jsonify({"message": "Please send valid data"}), 400

    name = data["name"]
    email = data["email"]
    password = data["password"]

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    try:
        sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        values = (name, email, hashed_password)

        cursor.execute(sql, values)
        db.commit()

        return jsonify({"message": "Signup successful!"})

    except:
        return jsonify({"message": "Email already exists!"}), 409




@app.route("/users", methods=["GET"])
def get_users():
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    return jsonify(users)


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if not data or "email" not in data or "password" not in data:
        return jsonify({"message": "Please send valid data"}), 400

    email = data["email"]
    password = data["password"]

    sql = "SELECT * FROM users WHERE email = %s"
    cursor.execute(sql, (email,))
    user = cursor.fetchone()

    if not user:
        return jsonify({"message": "User not found"}), 404

    stored_password = user["password"]

    if bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8") if isinstance(stored_password, str) else stored_password):
        return jsonify({
            "message": "Login successful!",
            "user": {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"]
            }
        })

    else:
        return jsonify({"message": "Invalid password"}), 401


if __name__ == "__main__":
    app.run(port=4000, debug=True)


