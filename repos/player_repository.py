from db/run_sql import run_sql

from models/player import Player
from models/character import Character

def save(player):

def select_all():

def select(id):

def delete_all():

def delete_id():

def update(player):

def characters(player):
    characters = []

    sql = "SELECT FROM characters WHERE player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)

    for row in results:
        character = Character(row['name'], row['race'], row['archetype'], row['level'], row['player_id'], row['party_id'], row['id'])
        characters.append(character)
    return characters