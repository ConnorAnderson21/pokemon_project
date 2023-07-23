from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


catch_poke = db.Table(
    'catch_poke',
    db.Column('user', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('pokemon', db.Integer, db.ForeignKey('pokemon.id'), nullable=False))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    wins = db.Column(db.Integer)
    loses = db.Column(db.Integer)

    

    def __init__(self,username, email, password, wins, loses):
        self.username = username
        self.email = email
        self.password = password
        self.wins = wins
        self.loses = loses

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def catch_it(self, pokemon):
        self.caught_poke.append(pokemon)
        db.session.commit()

    def release_it(self, pokemon):
        self.caught_poke.remove(pokemon)
        db.session.commit()

    def winning(self):
        self.wins += 1
        db.session.commit()

    def losing(self):
        self.loses -= 1
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
    price = db.Column(db.Numeric(12,2))

    caught_poke = db.relationship('User', 
        secondary = 'catch_poke',
        backref = 'caught_poke',
        lazy = 'dynamic'
            )                      


    def __init__(self, name, ability, base_exp, sprite, attack, defense, hp):
        self.name = name
        self.ability = ability
        self.base_exp = base_exp
        self.sprite = sprite
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.price = (base_exp) + hp + attack + defense 
        

    def save_pokemon(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ability': self.ability,
            'base_exp': self.base_exp,
            'sprite': self.sprite,
            'attack': self.attack,
            'defense': self.defense,
            'hp': self.hp,
            'price': self.price

        }


    


# need function to catch pokemon likes from class notes
# week 6 day1 tuesday backref