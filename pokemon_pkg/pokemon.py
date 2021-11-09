class Pokemon:
    def __init__(self, name, hp, attack, speed, type, type_icon, weaknesses):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.knocked_out = False
        self.attack = attack
        self.speed = speed
        self.type = type
        self.type_icon = type_icon
        self.weaknesses = weaknesses

    def get_name(self):
        return self.name

    def get_attack(self):
        return self.attack

    def get_type(self):
        return self.type

    def get_type_icon(self):
        return self.type_icon

    def get_hp_status(self):
        return f"{self.current_hp}/{self.max_hp} HP"


pokemon_list = {
    "Gengar": {
        "name": "Gengar",
        "hp": 165,
        "attack": 75,
        "speed": 100,
        "type": "psychic",
        "type_icon": "🔮",
        "weaknesses": "psychic"
    },
    "Charizard": {
        "name": "Charizard",
        "hp": 200,
        "attack": 90,
        "speed": 75,
        "type": "fire",
        "type_icon": "🔥",
        "weaknesses": "water"
    },
    "Blastoise": {
        "name": "Blastoise",
        "hp": 185,
        "attack": 80,
        "speed": 70,
        "type": "water",
        "type_icon": "💧",
        "weaknesses": "grass"
    },
    "Venasaur": {
        "name": "Venasaur",
        "hp": 180,
        "attack": 80,
        "speed": 70,
        "type": "grass",
        "type_icon": "🍃",
        "weaknesses": "fire"
    },
}

type_icons = {
    "fire": "🔥",
    "grass": "🍃",
    "psychic": "🔮",
    "water": "💧",
}


def build_pokemon_roster():
    # building a list of all possible pokemon to choose from this game
    pokemon_roster = {}
    for name, stats in pokemon_list.items():
        # pokemon constructor: name, hp, attack, speed, type, weakness
        # add to pokemon_roster pokemon of class Pokemon using the pokemon_list for the data
        pokemon_roster[name] = Pokemon(stats["name"], stats["hp"], stats["attack"], stats["speed"], stats["type"], stats["type_icon"], stats["weaknesses"])
    return pokemon_roster


def list_pokemon_stats():
    print(" ----------------------------------- POKEMON STATS ------------------------------------\n ")
    for i, pokemon in enumerate(pokemon_list):
        formatted_pokemon_name = pokemon
        while len(formatted_pokemon_name) < 9:
            formatted_pokemon_name += " "
        stats = pokemon_list[pokemon]
        print(
            f"{i + 1}) {formatted_pokemon_name} | HP: {stats['hp']} | ATTACK: {stats['attack']} | SPEED: {stats['speed']} | TYPE {stats['type']} {stats['type_icon']} | WEAKNESSES: {stats['weaknesses']} {type_icons[stats['weaknesses']]}")
    print(" \n-------------------------------------------------------------------------------------- ")
