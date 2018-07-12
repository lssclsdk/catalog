#!/usr/bin/python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # created table user with tablename user
    ids = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Games(Base):
    __tablename__ = 'games'
    # created table Games with tablename games
    ids = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.ids'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.ids,
        }


class Items(Base):
    __tablename__ = 'item'
    # created table Items with tablename item
    name = Column(String(80), nullable=False)
    ids = Column(Integer, primary_key=True)
    description = Column(String(250))
    game_id = Column(Integer, ForeignKey('games.ids'))
    game = relationship(Games)
    user_id = Column(Integer, ForeignKey('user.ids'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.ids,
            }


engine = create_engine('sqlite:///gameItem.db')


Base.metadata.create_all(engine)
