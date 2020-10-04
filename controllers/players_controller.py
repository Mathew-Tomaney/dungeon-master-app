from flask import Blueprint, Flask, redirect, render_template, request

import repos.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

# index
@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players=players)
# show
# new
# create
# edit
# update
# delete