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

party_2 = Party("Argyle & Associates", "Friday")
party_repository.save(party_2)

player_1 = Player("Dafyd", "Dungynmaestrr", "Dafyd@dragonmail.com")
player_repository.save(player_1)

player_2 = Player("Vin", "Diesel", "XXX@witchhunter.com")
player_repository.save(player_2)

player_3 = Player("Wil", "Wheaton", "shutup@wesley.com")
player_repository.save(player_3)

player_4 = Player("Joe", "Manganiello", "werewolvesrule@vampiressuck.com")
player_repository.save(player_4)

character_1 = Character("Duirric 'Dusty' Glenfoot", "Halfling", "Rogue", 11, player_1, party_1)
character_repository.save(character_1)

character_2 = Character("Argyle", "Tiefling", "Sorcerer", 5, player_2, party_2)
character_repository.save(character_2)

character_3 = Character("Thundrik Hopphammer", "Dwarf", "Cleric", 5, player_1, party_2)
character_repository.save(character_3)

character_4 = Character("Droop", "Goblin", "Fighter", 1, player_3, party_2)
character_repository.save(character_4)

character_5 = Character("Stormchaser", "Goliath", "Paladin", 12, player_4, party_1)
character_repository.save(character_5)

pdb.set_trace()