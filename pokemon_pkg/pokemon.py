class Pokemon:
    def __init__(self, name, hp, attack, speed, type, weaknesses):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.speed = speed
        self.type = type
        self.weaknesses = weaknesses

    def get_name(self):
        return self.name

    def get_attack(self):
        return self.attack


pokemon_list = {
    "Gengar": {
        "name": "Gengar",
        "hp": 150,
        "attack": 60,
        "speed": 100,
        "type": "psychic",
        "weaknesses": "psychic"
    },
    "Charizard": {
        "name": "Charizard",
        "hp": 200,
        "attack": 90,
        "speed": 75,
        "type": "fire",
        "weaknesses": "water"
    },
    "Blastoise": {
        "name": "Blastoise",
        "hp": 185,
        "attack": 80,
        "speed": 70,
        "type": "fire",
        "weaknesses": "grass"
    },
    "Venasaur": {
        "name": "Venasaur",
        "hp": 180,
        "attack": 80,
        "speed": 70,
        "type": "grass",
        "weaknesses": "fire"
    },
}


def build_pokemon_roster():
    # building a list of all possible pokemon to choose from this game
    pokemon_roster = {}
    for name, stats in pokemon_list.items():
        # pokemon constructor: name, hp, attack, speed, type, weakness
        # add to pokemon_roster pokemon of class Pokemon using the pokemon_list for the data
        pokemon_roster[name] = Pokemon(stats["name"], stats["hp"], stats["attack"], stats["speed"], stats["type"], stats["weaknesses"])
    return pokemon_roster
