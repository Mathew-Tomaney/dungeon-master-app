from db/run_sql import run_sql

from models/party import Party

def save(party):

def select_all():

def select(id):

def delete_all():

def delete_id():

def update(party):

def characters(party):
    characters = []

    sql = "SELECT FROM characters WHERE party_id = %s"
    values = [author.id]
    results = run_sql(sql, values)

    for row in results:
        character = Character(row['name'], row['race'], row['archetype'], row['level'], row['player_id'], row['party_id'], row['id'])
        characters.append(character)
    return characters