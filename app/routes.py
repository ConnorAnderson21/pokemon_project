from app import app

from flask import render_template

@app.route('/')
def land():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/team')
def team():
    team_list = current_user.catch_poke
    return render_template('team.html', team_list=team_list)

@app.route('/arena')
def arena():
    team_list = current_user.catch_poke
    return render_template('arena.html', team_list=team_list)



# @app.route('/team/')
# def team():
#     pokemon_list = current_user.catching.limit(6).all()
#     return render_template('team.html', p_list=pokemon_list)
