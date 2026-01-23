from flask import Flask, request, jsonify
import random

app = Flask(__name__)


books = [
    {"id": "1", "name": "Data Structures", "author": "Mark Allen Weiss"},
    {"id": "2", "name": "Operating System", "author": "Abraham Silberschatz"}

]



@app.route("/", methods=["GET"])
def serve_home():
    return "<h1>Welcome to API by Akash</h1>"



@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify(books)



@app.route("/book/<id>", methods=["GET"])
def get_one_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return jsonify({"message": "No book found with given Id"})



@app.route("/book", methods=["POST"])
def add_one_book():
    data = request.json

    if not data or "name" not in data or "author" not in data:

        return jsonify({"message": "Please send valid data"})

    new_book = {
        "id": str(random.randint(1, 100)),
        "name": data["name"],
        "author": data["author"]
    }

    books.append(new_book)
    return jsonify(new_book)



@app.route("/books/<id>", methods=["PUT"])
def update_one_book(id):
    data = request.json

    for index, book in enumerate(books):
        if book["id"] == id:
            books[index] = {
                "id": id,
                "name": data["name"],
                "author": data["author"]
            }
            return jsonify(books[index])

    return jsonify({"message": "book not found"})



@app.route("/books/<id>", methods=["DELETE"])
def delete_one_book(id):
    for index, book in enumerate(books):
        if book["id"] == id:
            books.pop(index)
            return jsonify({"message": "book deleted"})

    return jsonify({"message": "book not found"})


if __name__ == "__main__":
    app.run(port=4000, debug=True)
