import unittest

from models.character import Character
from models.player import Player
from models.party import Party


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Dafyd", "Dungynmaestrr", "Dafyd@dragonmail.com", 2)
        self.party_1 = Party("Barovian Basterds", "2020.10.04", 4)
        self.character_1 = Character("Duirric 'Dusty' Glenfoot", "Halfling", "Rogue", 11, 18, True, 80, 20, 12, "Brave: advantage against frightened", "Normal", "Thieves Cant", None, "The law", 0, self.player_1, self.party_1)


    def test_character_has_name(self):
        self.assertEqual("Duirric 'Dusty' Glenfoot", self.character_1.name)

    def test_character_has_race(self):
        self.assertEqual("Halfling", self.character_1.race)
    
    def test_character_has_archetype(self):
        self.assertEqual("Rogue", self.character_1.archetype)
    
    def test_character_has_level(self):
        self.assertEqual(11, self.character_1.level)
    
    def test_character_has_player_id(self):
        self.assertEqual(2, self.character_1.player.id)
    
    def test_character_has_party_id(self):
        self.assertEqual(4, self.character_1.party.id)
    
    def test_character_has_no_id_at_start(self):
        self.assertEqual(None, self.character_1.id)
    
    def test_character_can_have_id(self):
        self.character_2 = Character("Stormchaser", "Goliath", "Paladin", 11, 21, True, 200, 14, 16, "Immune to Cold", "Truesight 60ft", "Giant", "Aura of Protection 10ft", "Criminals", 1, 3, 5, 7)
        self.assertEqual(7, self.character_2.id)

    def test_character_has_armour(self):
        self.assertEqual(18, self.character_1.armour)

    def test_character_has_magic(self):
        self.assertEqual(True, self.character_1.magic)

    def test_character_has_weight(self):
        self.assertEqual(80, self.character_1.weight)

    def test_character_has_perception(self):
        self.assertEqual(20, self.character_1.perception)

    def test_character_has_insight(self):
        self.assertEqual(12, self.character_1.insight)

    def test_character_has_immunity(self):
        self.assertEqual("Brave: advantage against frightened", self.character_1.immunity)

    def test_character_has_vision(self):
        self.assertEqual("Normal", self.character_1.vision)

    def test_character_has_language(self):
        self.assertEqual("Thieves Cant", self.character_1.language)

    def test_character_has_aura(self):
        self.assertEqual(None, self.character_1.aura)

    def test_character_has_enmity(self):
        self.assertEqual("The law", self.character_1.enmity)

    def test_character_has_exhaustion(self):
        self.assertEqual(0, self.character_1.exhaustion)

