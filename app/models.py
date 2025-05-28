from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///movie.db')
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    watches = relationship('Watch', back_populates='user')

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    year = Column(Integer)

    watches = relationship('Watch', back_populates='movie')

class Site(Base):
    __tablename__ = 'sites'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subscription_fee = Column(Float)

    watches = relationship('Watch', back_populates='site')

class Watch(Base):
    __tablename__ = 'watches'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    site_id = Column(Integer, ForeignKey('sites.id'))
    watched_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='watches')
    movie = relationship('Movie', back_populates='watches')
    site = relationship('Site', back_populates='watches')
