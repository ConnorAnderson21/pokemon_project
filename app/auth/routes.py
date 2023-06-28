from flask import Blueprint, render_template, request, redirect, url_for, flash

from .forms import PokeName, SignupForm, LoginForm
from ..models import User

import requests, json

auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/enterpokemon', methods=['GET', 'POST'])
def enterpokemon():
    form = PokeName()
    # print(request.method)
    if request.method == 'POST':

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
        flash(f'Wild {pokemon.capitalize()} Appeared!')        
        return render_template('enterpokemon.html', form=form, poke=poke)
    # flash(f'Wild {pokemon} Appeared!')
    return render_template('enterpokemon.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User(username, email, password)
            user.save_user()
            return redirect(url_for('auth.login'))



    return render_template('signup.html', form=form)

    
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data


    return render_template('login.html', form=form)
