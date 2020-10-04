from flask import Blueprint, Flask, redirect, render_template, request

from models.player import Player
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
@players_blueprint.route("/players/new")
def new_player():
    return render_template("/players/new.html")

# create
@players_blueprint.route("/players", methods=["POST"])
def create_player():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    new_player = Player(first_name, last_name, email)
    new_player_with_id = player_repository.save(new_player)
    return redirect("players/<new_player_with_id.id>")

# edit
@players_blueprint.route("/players/<id>/edit")
def edit_player(id):
    player = player_repository.select(id)
    return render_template("/players/edit.html", player=player)

# update
@players_blueprint.route("/players/<id>", methods=["POST"])
def update_player(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    player = Player(first_name, last_name, email, id)
    player_repository.update(player)
    return redirect("/players/<id>")

# delete
@players_blueprint.route("/players/<id>/delete", methods=["POST"])
def delete_player(id):
    player_repository.delete_id(id)
    return redirect("/players")