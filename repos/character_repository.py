from db.run_sql import run_sql

from models.character import Character
from models.player import Player
from models.party import Party

import repos.party_repository as party_repository
import repos.player_repository as player_repository


def save(character):
    sql = "INSERT INTO characters (name, race, archetype, level, player_id, party_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [character.name, character.race, character.archetype, character.level, character.player.id, character.party.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    character.id = id


def select_all():
    characters = []

    sql = "SELECT * FROM characters"
    results = run_sql(sql)

    for result in results:
        player = player_repository.select(result["player_id"])
        party = party_repository.select(result["party_id"])
        character = Character(result['name'], result['race'], result['archetype'], result['level'], player, party, result['id'])
        characters.append(character)
    return characters

def select(id):
    character = None
    sql = "SELECT * FROM characters WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    player = player_repository.select(result["player_id"])
    party = party_repository.select(result["party_id"])

    if result is not None:
        character = Character(result['name'], result['race'], result['archetype'], result['level'], player, party, result['id'])
    return character

def delete_all():
    sql = "DELETE FROM characters"
    run_sql(sql)

def delete_id(id):
    sql = "DELETE FROM characters WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(character):
    sql = "UPDATE characters SET (name, race, archetype, level, player_id, party_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [character.name, character.race, character.archetype, character.level, character.player.id, character.party.id]
    run_sql(sql, values)