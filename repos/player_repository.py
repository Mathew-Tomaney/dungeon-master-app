from db.run_sql import run_sql

from models.player import Player
from models.character import Character
from models.party import Party
import repos.party_repository as party_repository
import repos.player_repository as player_repository

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
    sql = "UPDATE players SET (first_name, last_name, email) = (%s, %s, %s) WHERE id = %s"
    values = [player.first_name, player.last_name, player.email, player.id]
    run_sql(sql, values)

def characters(id):
    player_characters = []
    sql = "SELECT characters.* FROM characters WHERE player_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        player = player_repository.select(id)
        party = party_repository.select(result['party_id'])
        character = Character(result['name'], result['race'], result['archetype'], result['level'], result['armour'], result['magic'], result['weight'], result['perception'], result['insight'], result['immunity'], result['vision'], result['language'], result['aura'], result['enmity'], result['exhaustion'], player, party, result['id'])
        player_characters.append(character)
    return player_characters

def parties(id):
    player_parties = []
    sql = "SELECT parties.* FROM parties INNER JOIN characters ON characters.party_id = parties.id WHERE characters.player_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        party = Party(result["name"], result["next_game"], result["id"])
        player_parties.append(party)
    return player_parties