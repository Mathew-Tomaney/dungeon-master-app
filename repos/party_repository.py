from db.run_sql import run_sql

from models.party import Party
from models.character import Character
from models.player import Player
import repos.player_repository as player_repository
import repos.party_repository as party_repository

def save(party):
    sql = "INSERT INTO parties (name, next_game) VALUES (%s, %s) RETURNING *"
    values = [party.name, party.next_game]
    results = run_sql(sql, values)
    id = results[0]['id']
    party.id = id


def select_all():
    parties = []

    sql = "SELECT * FROM parties"
    results = run_sql(sql)

    for result in results:
        party = Party(result['name'], result['next_game'], result['id'] )
        parties.append(party)
    return parties

def select(id):
    party = None
    sql = "SELECT * FROM parties WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        party = Party(result['name'], result['next_game'], result['id'] )
    return party

def delete_all():
    sql = "DELETE FROM parties"
    run_sql(sql)

def delete_id(id):
    sql = "DELETE FROM parties WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(party):
    sql = "UPDATE parties SET (name, next_game) = (%s, %s) WHERE id = %s"
    values = [party.name, party.next_game, party.id]
    run_sql(sql, values)

def characters(id):
    characters_in_party = []
    sql = "SELECT characters.* FROM characters WHERE party_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        party = party_repository.select(id)
        player = player_repository.select(result['player_id'])
        character = Character(result['name'], result['race'], result['archetype'], result['level'], player, party, result['id'])
        characters_in_party.append(character)
    return characters_in_party

def players(id):
    players_in_party = []
    sql = "SELECT players.* FROM players INNER JOIN characters ON characters.player_id = players.id WHERE characters.party_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        player = Player(result["first_name"], result["last_name"], result["email"], result["id"])
        players_in_party.append(player)
    return players_in_party