from flask import Blueprint, Flask, redirect, render_template, request, flash

from models.character import Character
import repos.character_repository as character_repository
import repos.party_repository as party_repository
import repos.player_repository as player_repository

characters_blueprint = Blueprint("characters", __name__)

# index
@characters_blueprint.route("/characters")
def characters():
    characters = character_repository.select_all()
    characters.sort(key=lambda character: character.name)
    players = player_repository.select_all()
    parties = party_repository.select_all()

    return render_template("characters/index.html", characters=characters, players=players, parties=parties)

# show
@characters_blueprint.route("/characters/<id>")
def show_characters(id):
    character = character_repository.select(id)
    player = player_repository.select(character.player.id)
    party = party_repository.select(character.party.id)
    return render_template("/characters/show.html", character=character, player=player, party=party)

# new
@characters_blueprint.route("/characters/new/<name_choice>")
def new_character(name_choice):
    players = player_repository.select_all()
    parties = party_repository.select_all()
    return render_template("/characters/new.html", players=players, parties=parties, name_choice=name_choice)

# create
@characters_blueprint.route("/characters", methods=["POST"])
def create_character():
    name = request.form["name"]
    race = request.form["race"]
    archetype = request.form["archetype"]
    level = request.form["level"]
    armour = request.form["armour"]
    magic = request.form["magic"]
    weight = request.form["weight"]
    perception = request.form["perception"]
    insight = request.form["insight"]
    immunity = request.form["immunity"]
    vision = request.form["vision"]
    language = request.form["language"]
    aura = request.form["aura"]
    enmity = request.form["enmity"]
    exhaustion = request.form["exhaustion"]
    player_id = request.form["player_id"]
    party_id = request.form["party_id"]
    player = player_repository.select(player_id)
    party = party_repository.select(party_id)
    new_character = Character(name, race, archetype, level, armour, magic, weight, perception, insight, immunity, vision, language, aura, enmity, exhaustion, player, party)
    character_repository.save(new_character)
    return redirect("/characters")

# edit
@characters_blueprint.route("/characters/<id>/edit")
def edit_character(id):
    character = character_repository.select(id)
    parties = party_repository.select_all()
    players = player_repository.select_all()
    return render_template("/characters/edit.html", character=character, players=players, parties=parties)

# update
@characters_blueprint.route("/characters/<id>", methods=["POST"])
def update_character(id):
    name = request.form["name"]
    race = request.form["race"]
    archetype = request.form["archetype"]
    level = request.form["level"]
    armour = request.form["armour"]
    magic = request.form["magic"]
    weight = request.form["weight"]
    perception = request.form["perception"]
    insight = request.form["insight"]
    immunity = request.form["immunity"]
    vision = request.form["vision"]
    language = request.form["language"]
    aura = request.form["aura"]
    enmity = request.form["enmity"]
    exhaustion = request.form["exhaustion"]
    player_id = request.form["player_id"]
    party_id = request.form["party_id"]
    player = player_repository.select(player_id)
    party = party_repository.select(party_id)
    character = Character(name, race, archetype, level, armour, magic, weight, perception, insight, immunity, vision, language, aura, enmity, exhaustion, player, party, id)
    character_repository.update(character)
    return show_characters(character.id)

# delete
@characters_blueprint.route("/characters/<id>/delete", methods=["POST"])
def delete_character(id):
    character_repository.delete_id(id)
    return redirect("/characters")

@characters_blueprint.route("/characters/check", methods=["POST"])
def check_name():
    name_choice = request.form["name"]
    name_exists_id = character_repository.check(name_choice)
    if name_exists_id is False and name_choice is not "":
        return redirect(f"/characters/new/{name_choice}")
        # players = player_repository.select_all()
        # parties = party_repository.select_all()
        # return render_template("/characters/new.html", players=players, parties=parties, name_choice=name_choice)
    else: flash("This adventurer already exists! Pick a new name!")
    return redirect("/characters")
    