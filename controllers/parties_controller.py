from flask import Blueprint, Flask, redirect, render_template, request

from models.party import Party
import repos.party_repository as party_repository
# import repos.player_repository as player_repository
# import repos.character_repository as character_repository


parties_blueprint = Blueprint("parties", __name__)

# index
@parties_blueprint.route("/parties")
def parties():
    parties = party_repository.select_all()
    parties.sort(key=lambda party: party.name)
    return render_template("parties/index.html", parties=parties)

# show
@parties_blueprint.route("/parties/<id>")
def show_parties(id):
    party = party_repository.select(id)
    players = party_repository.players(id)
    characters = party_repository.characters(id)
    num_of_players = len(party_repository.players(party.id))
    average_level = party_repository.party_level(id)
    lowest_armour = party_repository.lowest_armour(id)
    all_contacts = party_repository.all_contact(id)
    highest_perception = party_repository.highest_perception(id)
    highest_insight = party_repository.highest_insight(id)
    total_weight = party_repository.total_weight(id)
    magic_percent = party_repository.party_magic_compare(id)
    return render_template("/parties/show.html", party=party, players=players, characters=characters, num_of_players=num_of_players, average_level=average_level, lowest_armour=lowest_armour, all_contacts=all_contacts, highest_perception=highest_perception, highest_insight=highest_insight, total_weight=total_weight, magic_percent=magic_percent)

# new
@parties_blueprint.route("/parties/new")
def new_party():
    return render_template("/parties/new.html")

# create
@parties_blueprint.route("/parties", methods=["POST"])
def create_party():
    name = request.form["name"]
    next_game = request.form["next_game"]
    new_party = Party(name, next_game)
    party_repository.save(new_party)
    return redirect("/parties")

# edit
@parties_blueprint.route("/parties/<id>/edit")
def edit_party(id):
    party = party_repository.select(id)
    return render_template("/parties/edit.html", party=party)

# update
@parties_blueprint.route("/parties/<id>", methods=["POST"])
def update_party(id):
    name = request.form["name"]
    next_game = request.form["next_game"]
    party = Party(name, next_game, id)
    party_repository.update(party)
    return show_parties(party.id)

# delete
@parties_blueprint.route("/parties/<id>/delete", methods=["POST"])
def delete_party(id):
    party_repository.delete_id(id)
    return redirect("/parties")