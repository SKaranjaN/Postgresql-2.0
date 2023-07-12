from app import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    pages = db.Column(db.Integer)
    published = db.Column(db.Date)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', pages={self.pages}, published={self.published})>"