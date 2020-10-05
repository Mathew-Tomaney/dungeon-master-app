class Character:
    def __init__(self, name, race, archetype, level, armour, magic, weight, perception, insight, immunity, vision, language, aura, enmity, exhaustion=0, player, party, id=None):
        self.name = name
        self.race = race
        self.archetype = archetype
        self.level = level
        self.armour = armour
        self.magic = magic
        self.weight = weight
        self.perception = perception
        self.insight = insight
        self.immunity = immunity
        self.vision = vision
        self.language = language
        self.aura = aura
        self.enmity = enmity
        self.exhaustion = exhaustion
        self.player = player
        self.party = party
        self.id = id
