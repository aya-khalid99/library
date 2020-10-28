import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

# database_name = "library"
# database_path = "postgres://{}/{}".format('localhost:5432', database_name)
database_path = "postgresql://postgres:1999@localhost:5432/library"
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Techer(db.Model):
    __tablename__='techers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    specialty = Column(String)
    experience = Column(Integer)

    def __init__(self, name, age, specialty, experience):
        self.name = name
        self.age = age
        self.specialty = specialty
        self.experience = experience

    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'specialty': self.specialty,
            'experience': self.experience
        }


class Book(db.Model):
    __tablename__='books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    auther = Column(String)
    specialty = Column(String)
    number_of_pages = Column(Integer)

    def __init__(self, title, auther, number_of_pages, specialty):
        self.title = title
        self.auther = auther
        self.specialty = specialty
        self.number_of_pages = number_of_pages

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'auther': self.auther,
            'specialty': self.specialty,
            'number_of_pages': self.number_of_pages
        }



