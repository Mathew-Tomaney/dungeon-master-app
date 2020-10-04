from flask import Blueprint, Flask, redirect, render_template, request

import repos.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

# index
@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players=players)
    
# show
@players_blueprint.route("/players/<id>")
def show_player(id):
    player = player_repository.select(id)
    parties = player_repository.parties(id)
    characters = player_repository.characters(id)
    return render_template("/players/show.html", player=player, parties=parties, characters=characters)

# new
# create
# edit
# update
# delete