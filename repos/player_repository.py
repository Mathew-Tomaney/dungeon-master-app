from db.run_sql import run_sql

from models.player import Player
from models.character import Character

def save(player):
    sql = "INSERT INTO players (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING *"
    values = [player.first_name, player.last_name, player.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id


def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for result in results:
        player = Player(result['first_name'], result['last_name'], result['email'], result['id'] )
        players.append(player)
    return players

def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = Player(result['first_name'], result['last_name'], result['email'], result['id'] )
    return player

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def delete_id(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(player):
    sql = "UPDATE players SET (first_name, last_name, email) = (%s, %s %s) WHERE id = %s"
    values = [player.first_name, player.last_name, player.email, player.id]
    run_sql(sql, values)

def characters(player):
    characters = []

    sql = "SELECT FROM characters WHERE player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)

    for row in results:
        character = Character(row['name'], row['race'], row['archetype'], row['level'], row['player_id'], row['party_id'], row['id'])
        characters.append(character)
    return characters