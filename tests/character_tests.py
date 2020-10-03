import unittest

from models.character import Character


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character_1 = Character("Duirric 'Dusty' Glenfoot", "Halfling", "Rogue", 11, 2, 4)

    def test_character_has_name(self):
        self.assertEqual("Duirric 'Dusty' Glenfoot", self.character_1.name)

    def test_character_has_race(self):
        self.assertEqual("Halfling", self.character_1.race)
    
    def test_character_has_archetype(self):
        self.assertEqual("Rogue", self.character_1.archetype)
    
    def test_character_has_level(self):
        self.assertEqual(11, self.character_1.level)
    
    def test_character_has_player_id(self):
        self.assertEqual(2, self.character_1.player_id)
    
    def test_character_has_party_id(self):
        self.assertEqual(4, self.character_1.party_id)
    
    def test_character_has_no_id_at_start(self):
        self.assertEqual(None, self.character_1.id)