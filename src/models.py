import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()



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
        return {}


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False)
    favorites = db.relationship('Favorites')

    def __repr__(self):
        return f'<User {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "favorites": self.favorites
        }


class Character(Base):
    __tablename__= 'Character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    mass = db.Column(db.String(80), unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    homeworld = db.Column(db.String(80), unique=False, nullable=False)
    films = db.Column(db.String(80), unique=False, nullable=False)
    species = db.Column(db.String(80), unique=False, nullable=False)
    vehicles = db.Column(db.String(80), unique=False, nullable=False)
    starships = db.Column(db.String(80), unique=False, nullable=False)
    created = db.Column(db.String(80), unique=False, nullable=False)
    edited = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'<Character {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "films": self.films,
            "species": self.species,
            "vehicles": self.vehicles,
            "starships": self.starships,
            "created": self.created,
            "edited": self.edited,
            "url": self.url
           
        }

class Planet(db.Model):
    __tablename__ = 'Planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    rotation_period = db.Column(db.String(50), unique=False, nulable=False)
    diameter = db.Column(db.String(50), unique=False, nulable=False)
    climate = db.Column(db.String(90), unique=False, nulable=False)
    gravity = db.Column(db.String(30), unique=False, nulable=False)
    surface_water = db.Column(db.String(30), unique=False, nulable=False)
    residents = db.Column(db.String(50), unique=False, nulable=False)
    films = db.Column(db.String(50), unique=False, nulable=False)
    created = db.Column(db.String(50), unique=False, nulable=False)
    edited = db.Column(db.String(50), unique=False, nulable=False)
    url = db.Column(db.String(50), unique=False, nulable=False)

    
    def __repr__(self):
        return f'<Planet {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "surface_water": self.surface_water,
            "residents": self.residents,
            "films": self.films,
            "created": self.created,
            "edited": self.edited,
            "url": self.url,
          
        }

class Favorites(db.Model):
    __tablename__ = 'Favorites'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey ('Person.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey ('Planet.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    person = db.relationship('Person', lazy = True)
    planet = db.relationship('Planet', lazy = True)
    user = db.relationship('User', foreign_keys= [user_id])

    
    def __repr__(self):
       
        return f'<Favorites {self.person_id, self.planet_id}>'

    def serialize(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "planet_id": self.planet_id,
            "user_id": self.user_id
            
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')