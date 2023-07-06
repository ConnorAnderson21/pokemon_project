from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

# add join table is for catch

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Pokemon (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ability = db.Column(db.String, nullable=False)
    base_exp = db.Column(db.Integer, nullable=False)
    sprite = db.Column(db.String, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)

    def __init__(self, name, ability, base_exp, sprite, attack, defense, hp):
        self.name = name
        self.ability = ability
        self.base_exp = base_exp
        self.sprite = sprite
        self.attack = attack
        self.defense = defense
        self.hp = hp

    def save_pokemon(self):
        db.session.add(self)
        db.session.commit()




    


# need function to catch pokemon likes from class notes
# week 6 day1 tuesday backref