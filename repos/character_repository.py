from db.run_sql import run_sql

from models.character import Character

Character(row['name'], row['race'], row['archetype'], row['level'], row['player_id'], row['party_id'], row['id'])

def save(character):
    sql = "INSERT INTO characters (name, race, archetype, level, player_id, party_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [character.name, character.race, character.archetype, character.level, character.player.id, character.party.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    character.id = id
    return character


def select_all():
    characters = []

    sql = "SELECT * FROM characters"
    results = run_sql(sql)

    for row in results:
        character = Character(row['name'], row['race'], row['archetype'], row['level'], row['player_id'], row['party_id'], row['id'])
        characters.append(character)
    return characters

def select(id):
    character = None
    sql = "SELECT * FROM characters WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        character = Character(row['name'], row['race'], row['archetype'], row['level'], row['player_id'], row['party_id'], row['id'])
    return character

def delete_all():
    sql = "DELETE FROM characters"
    run_sql(sql)

def delete_id():
    sql = "DELETE FROM characters WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(character):
    sql = "UPDATE characters SET (name, race, archetype, level, player_id, party_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [character.name, character.race, character.archetype, character.level, character.player.id, character.party.id]
    run_sql(sql, values)