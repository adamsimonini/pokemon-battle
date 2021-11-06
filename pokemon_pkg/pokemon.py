class Pokemon:
    def __init__(self, name, hp, attack, speed, type, weakness):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.type = type
        self.weakness = weakness

    def get_name(self):
        return self.name


pokemon_list = {
    "Gengar": {
        "hp": 150,
        "attack": 60,
        "speed": 100,
        "type": "psychic",
        "weakness": "psychic"
    },
    "Charizard": {
        "hp": 200,
        "attack": 90,
        "speed": 75,
        "type": "fire",
        "weakness": "water"
    },
    "Blastoise": {
        "hp": 185,
        "attack": 80,
        "speed": 70,
        "type": "fire",
        "weakness": "grass"
    },
    "Venasaur": {
        "hp": 180,
        "attack": 80,
        "speed": 70,
        "type": "grass",
        "weakness": "fire"
    },
}
