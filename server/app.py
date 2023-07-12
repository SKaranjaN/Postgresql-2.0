from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Book  

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/books', methods=['GET'])
def book():
    books = Book.query.all()
    all_books = []

    for book in books:
        book_dict = {
            "id" : book.id,
            "title": book.title,
            "author": book.author,
            "pages": book.pages,
            "published": book.published
        }
        all_books.append(book_dict)

        response = make_response(jsonify(all_books), 200)
        return response

if __name__ == '__main__':
    app.run()