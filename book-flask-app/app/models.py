from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
   
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    author = db.Column(db.String(120))

    def __init__(self, title=None, author=None):
        self.title = title
        self.author = author