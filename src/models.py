import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String (200), nullable=False)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    comment = relationship('Comment')
    post = relationship('Post')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    user = relationship('User')
    post = relationship('Post')

class Post(Base):
    __tablename__ = 'posts'
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    comments = relationship("Comment")
    media = relationship('Media')
    
class Media(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    type = Column(String (200), nullable=False)
    url = Column(String(200), nullable=False)
    post_id= Column(Integer,  ForeignKey('posts.id'))
    post = relationship('Post')

class Follower(Base):
    __tablename__ = 'followers'
    user_from_id= Column(Integer, ForeignKey('users.id'), primary_key=True)
    user_to_id= Column(Integer, ForeignKey('users.id'), primary_key=True)
    user = relationship('User')











## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
