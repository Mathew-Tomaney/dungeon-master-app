class Character:
    def __init__(self, name, race, archetype, level, player_id, party_id, id=None):
        self.name = name
        self.race = race
        self.archetype = archetype
        self.level = level
        self.player_id = player_id
        self.party_id = party_id
        self.id = id