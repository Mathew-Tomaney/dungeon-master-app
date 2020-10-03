import unittest

from models.party import Party

class TestParty(unittest.TestCase):
    def setUp(self):
        self.party_1 = Party("Barovian Basterds", "2020.10.04")

    def test_party_has_name(self):
        self.assertEqual("Barovian Basterds", self.party_1.name)
    
    def test_party_has_next_game(self):
        self.assertEqual("2020.10.04", self.party_1.next_game)
    
    def test_party_has_no_id_at_start(self):
        self.assertEqual(None, self.party_1.id)