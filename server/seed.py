from app import app, db
from models import Book

with app.app_context():
    db.create_all()

    book1 = Book(title='Book 1', author='Author 1', pages=100, published='2022-01-01')
    book2 = Book(title='Book 2', author='Author 2', pages=200, published='2022-02-01')
    db.session.add_all([book1, book2])
    db.session.commit()