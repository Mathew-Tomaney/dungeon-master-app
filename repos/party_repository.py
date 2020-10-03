from db/run_sql import run_sql

from models/party import Party
from models/character import Character

def save(party):
    sql = "INSERT INTO parties (name, next_game) VALUES (%s, %s) RETURNING *"
    values = [party.name, party.next_game]
    results = run_sql(sql, values)
    id = results[0]['id']
    party.id = id
    return party


def select_all():
    parties = []

    sql = "SELECT * FROM parties"
    results = run_sql(sql)

    for row in results:
        party = Party(row['name'], row['next_game'], row['id'] )
        parties.append(party)
    return parties

def select(id):
    party = None
    sql = "SELECT * FROM parties WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        party = Party(result['name'], result['last_name'], result['id'] )
    return party

def delete_all():
    sql = "DELETE FROM parties"
    run_sql(sql)

def delete_id():
    sql = "DELETE FROM parties WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(party):
    sql = "UPDATE parties SET (name, next_game) = (%s, %s) WHERE id = %s"
    values = [party.name, party.next_game, party.id]
    run_sql(sql, values)

def characters(party):
    characters = []

    sql = "SELECT FROM characters WHERE party_id = %s"
    values = [party.id]
    results = run_sql(sql, values)

    for row in results:
        character = Character(row['name'], row['race'], row['archetype'], row['level'], row['player_id'], row['party_id'], row['id'])
        characters.append(character)
    return characters