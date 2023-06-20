from flask import Blueprint, render_template, request, redirect, url_for

from .forms import PokeName

import requests, json

auth = Blueprint('auth', __name__, template_folder='auth_templates')




@auth.route('/enterpokemon', methods=['GET', 'POST'])
def enterpokemon():
    form = PokeName()
    # print(request.method)
    if request.method == 'POST':
        if form.validate():
            pokemon = form.pokemon.data
            print(pokemon)
            def poke_data(pokename):
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokename}")
                print(response)
                if response.ok:
                    data = response.json()
                    pokeinfo = {}
                    pokeinfo['species'] = pokename
                    pokeinfo['ability'] = data["abilities"][0]['ability']['name']
                    pokeinfo['base_exp'] = data["base_experience"]
                    pokeinfo['sprite'] = data['sprites']['front_shiny']
                    pokeinfo['attack'] = data['stats'][1]['base_stat']
                    pokeinfo['defense'] = data['stats'][2]['base_stat']
                    pokeinfo['hp'] = data['stats'][0]['base_stat']
                    return pokeinfo
            poke = poke_data(pokemon)
            print(poke)
            return render_template('enterpokemon.html', form=form, poke=poke)
    return render_template('enterpokemon.html', form=form)


    
 