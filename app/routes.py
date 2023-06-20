from app import app

from flask import render_template

@app.route('/')
def land():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/poke_data')
def poke_data(pokename):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokename}")
    if response.ok:
        data = response.json()
        pokeinfo = {}
#         my_team = []
        pokeinfo['species'] = pokename
        pokeinfo['ability'] = data["abilities"][0]['ability']['name']
        pokeinfo['base_exp'] = data["base_experience"]
        pokeinfo['sprite'] = data['sprites']['front_shiny']
        pokeinfo['attack'] = data['stats'][1]['base_stat']
        pokeinfo['defense'] = data['stats'][2]['base_stat']
        pokeinfo['hp'] = data['stats'][0]['base_stat']
        return pokeinfo
    return {}

