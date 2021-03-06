from db.run_sql import run_sql

from models.character import Character
from models.player import Player
from models.party import Party

import repos.party_repository as party_repository
import repos.player_repository as player_repository
import repos.character_repository as character_repository


def save(character):
    sql = "INSERT INTO characters (name, race, archetype, level, armour, magic, weight, perception, insight, immunity, vision, language, aura, enmity, exhaustion, player_id, party_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [character.name, character.race, character.archetype, character.level, character.armour, character.magic, character.weight, character.perception, character.insight, character.immunity, character.vision, character.language, character.aura, character.enmity, character.exhaustion, character.player.id, character.party.id]
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
        character = Character(result['name'], result['race'], result['archetype'], result['level'], result['armour'], result['magic'], result['weight'], result['perception'], result['insight'], result['immunity'], result['vision'], result['language'], result['aura'], result['enmity'], result['exhaustion'], player, party, result['id'])
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
        character = Character(result['name'], result['race'], result['archetype'], result['level'], result['armour'], result['magic'], result['weight'], result['perception'], result['insight'], result['immunity'], result['vision'], result['language'], result['aura'], result['enmity'], result['exhaustion'], player, party, result['id'])
    return character

def delete_all():
    sql = "DELETE FROM characters"
    run_sql(sql)

def delete_id(id):
    sql = "DELETE FROM characters WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(character):
    sql = "UPDATE characters SET (name, race, archetype, level, armour, magic, weight, perception, insight, immunity, vision, language, aura, enmity, exhaustion, player_id, party_id) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [character.name, character.race, character.archetype, character.level, character.armour, character.magic, character.weight, character.perception, character.insight, character.immunity, character.vision, character.language, character.aura, character.enmity, character.exhaustion, character.player.id, character.party.id, character.id]
    run_sql(sql, values)

def check(new_name):
    characters = character_repository.select_all()
    for character in characters:
        if character.name.lower() == new_name.lower():
            return character.id
    return False
