import pdb

from models.character import Character
from models.party import Party
from models.player import Player

import repos.character_repository as character_repository
import repos.party_repository as party_repository
import repos.player_repository as player_repository

character_repository.delete_all()
party_repository.delete_all()
player_repository.delete_all()

party_1 = Party("Barovian Basterds", "2020.10.04")
party_repository.save(party_1)

player_1 = Player("Dafyd", "Dungynmaestrr", "Dafyd@dragonmail.com")
player_repository.save(player_1)

character_1 = Character("Duirric 'Dusty' Glenfoot", "Halfling", "Rogue", 11, player_1, party_1)
character_repository.save(character_1)

pdb.set_trace()