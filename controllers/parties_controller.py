from flask import Blueprint, Flask, redirect, render_template, request

from models.parties import Party
import repos.party_repository as party_repository


parties_blueprint = Blueprint("parties", __name__)

# index
@parties_blueprint.route("/parties")
def parties():
    parties = parties_repository.select_all()
    return render_template("parties/index.html", parties=parties)

# show
@partiess_blueprint.route("/partiess/<id>")
def show_parties(id):
    parties = parties_repository.select(id)
    parties = parties_repository.parties(id)
    characters = parties_repository.characters(id)
    return render_template("/partiess/show.html", parties=parties, parties=parties, characters=characters)

# new
@partiess_blueprint.route("/partiess/new")
def new_parties():
    return render_template("/partiess/new.html")

# create
@partiess_blueprint.route("/partiess", methods=["POST"])
def create_parties():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    new_parties = parties(first_name, last_name, email)
    parties_repository.save(new_parties)
    return redirect("/partiess")

# edit
@partiess_blueprint.route("/partiess/<id>/edit")
def edit_parties(id):
    parties = parties_repository.select(id)
    return render_template("/partiess/edit.html", parties=parties)

# update
@partiess_blueprint.route("/partiess/<id>", methods=["POST"])
def update_parties(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    parties = parties(first_name, last_name, email, id)
    parties_repository.update(parties)
    return show_parties(parties.id)

# delete
@partiess_blueprint.route("/partiess/<id>/delete", methods=["POST"])
def delete_parties(id):
    parties_repository.delete_id(id)
    return redirect("/partiess")