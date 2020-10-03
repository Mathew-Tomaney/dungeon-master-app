class Character:
    def __init__(self, name, race, archetype, level, player, party, id=None):
        self.name = name
        self.race = race
        self.archetype = archetype
        self.level = level
        self.player = player
        self.party = party
        self.id = id