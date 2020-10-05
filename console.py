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

character_1 = Character("Duirric 'Dusty' Glenfoot", "Halfling", "Rogue", 11, 18, True, 80, 20, 12, "Brave: advantage against frightened", "Normal", "Thieves Cant", None, "The law", 0, player_1, party_1)
character_repository.save(character_1)

character_2 = Character("Argyle", "Tiefling", "Sorcerer", 5, 12, True, 90, 18, 16, "Immune to Fire", "Darkvision", "Infernal", None, "Lawful Good Alignment", 0, player_2, party_2)
character_repository.save(character_2)

character_3 = Character("Thundrik Hopphammer", "Dwarf", "Cleric", 5, 20, True, 100, 20, 16, "Immune to Poison", "Darkvision", "Gnomish", "Guidance on Touch", "Goblins", 0, player_1, party_2)
character_repository.save(character_3)

character_4 = Character("Droop", "Goblin", "Fighter", 1, 12, False, 70, 10, 10, None, "Normal", "Hobgoblin", None, "Dwarves", 1, player_3, party_2)
character_repository.save(character_4)

character_5 = Character("Stormchaser", "Goliath", "Paladin", 11, 21, True, 200, 14, 16, "Immune to Cold", "Truesight 60ft", "Giant", "Aura of Protection 10ft", "Criminals", 1, player_2, party_1)
character_repository.save(character_5)

character_6 = Character("Stormchaser", "Goliath", "Paladin/Fighter", 11, 21, True, 200, 14, 16, "Immune to Cold", "Truesight 60ft", "Giant", "Aura of Protection 10ft", "Criminals", 1, player_2, party_1, 5) 
character_repository.update(character_6)

pdb.set_trace()