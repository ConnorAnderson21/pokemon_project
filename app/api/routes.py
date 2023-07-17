from flask import Blueprint, request, json

from ..models import Pokemon

api = Blueprint('api', __name__, url_prefix='/api')


@api.get('/pokemon')
def get_pokemon():
    pokemon = Pokemon.query.all()
    pokemon_list = [p.to_dict() for p in pokemon]
    return {
        'status' : 'ok',
        'pokemon' : pokemon_list
    }

@api.get('/post/<int:poke_id>')
def get_poke_by_id(poke_id):
    poke = Pokemon.query.get(poke_id)
    if poke:
        return {
            'pokemon': poke.to_dict(),
            'status': 'ok'
        }
    else:
        return {
            'status' : 'NOT ok',
            'message' : 'there is no pokemon for that id'
        }
    
@api.get('/post/<poke_name>')
def get_poke_by_title(poke_name):
    poke = Pokemon.query.filter_by(name=poke_name).first()
    if poke:
        return {
            'pokemon': poke.to_dict(),
            'status': 'ok'
        }
    else:
        return {
            'status' : 'NOT ok',
            'message' : 'there is no pokemon for that name'
        }