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
        character = Character(result['name'], result['race'], result['archetype'], result['level'], result['armour'], result['magic'], result['weight'], result['perception'], result['insight'], result['immunity'], result['vision'], result['language'], result['aura'], result['enmity'], result['exhaustion'], player, party, result['id'])
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

def party_level(id):
    party_level = 0
    characters = party_repository.characters(id)
    levels = []
    for character in characters:
        levels.append(character.level)
        party_level = sum(levels)/len(levels)
    return round(party_level, 1)

def lowest_armour(id):
    lowest = 0
    total = []
    characters = party_repository.characters(id)
    for character in characters:
        total.append(character.armour)
    total.sort()
    if total is not None:
        lowest = total[0] 
    return lowest

def all_games():
    parties = party_repository.select_all()
    upcoming_games = []
    for party in parties:
        upcoming_games.append([party.name, party.next_game])
    return upcoming_games 

def all_contact(id):
    players = party_repository.players(id)
    contacts =[]
    for player in players:
        contacts.append(player.email)
    return contacts

def highest_perception(id):
    highest = 0
    characters = party_repository.characters(id)
    skills = []
    for character in characters:
        skills.append(character.perception)
    skills.sort()
    if skills is not None:
        highest = skills[-1]
    return highest

def highest_insight(id):
    highest = 0
    characters = party_repository.characters(id)
    skills = []
    for character in characters:
        skills.append(character.insight)
    skills.sort()
    if skills is not None:
        highest = skills[-1]
    return highest

def total_weight(id):
    all_weights = []
    characters = party_repository.characters(id)
    for character in characters:
        all_weights.append(character.weight)
    total_weight = sum(all_weights)
    return total_weight

def party_magic(id):
    has_magic = 0
    characters = party_repository.characters(id)
    for character in characters:
        if character.magic == True:
            has_magic += 1
    return has_magic

def party_magic_compare(id):
    magic_percent = (party_repository.party_magic(id) / len(party_repository.players(id))) * 100
    return round(magic_percent, 2)

