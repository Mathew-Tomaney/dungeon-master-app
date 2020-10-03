import unittest
 
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Dafyd", "Dungynmaestrr", "Dafyd@dragonmail.com")

    def test_player_has_first_name(self):
        self.assertEqual("Dafyd", self.player_1.first_name)

    def test_player_has_last_name(self):
        self.assertEqual("Dungynmaestrr", self.player_1.last_name)

    def test_player_has_email(self):
        self.assertEqual("Dafyd@dragonmail.com", self.player_1.email)
    
    def test_player_starts_no_id(self):
        self.assertEqual(None, self.player_1.id)

    def test_can_get_full_name(self):
        self.assertEqual("Dafyd Dungynmaestrr", self.player_1.full_name())