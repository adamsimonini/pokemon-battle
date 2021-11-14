class Pokemon:
    def __init__(self, name, hp, attack, speed):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.is_knocked_out = False
        self.attack = attack
        self.speed = speed

    def get_name(self):
        return self.name

    def get_attack(self):
        return self.attack

    def get_speed(self):
        return self.speed

    def get_hp_status(self):
        if self.current_hp > 0:
            return f"{self.name} has {self.current_hp}/{self.max_hp} HP remaining"
        return False

    def get_current_hp(self):
        return self.current_hp

    def set_hp(self, hp):
        self.current_hp = hp

    def get_knocked_out_status(self):
        return self.is_knocked_out


class Fire_Pokemon(Pokemon):
    def __init__(self, name, max_hp, attack, speed):
        super().__init__(name, max_hp, attack, speed)
        self.type = "fire"
        self.type_icon = "🔥"
        self.weakenesses = ["water"]


class Water_Pokemon(Pokemon):
    def __init__(self, name, max_hp, attack, speed):
        super().__init__(name, max_hp, attack, speed)
        self.type = "fire"
        self.type_icon = "💧"
        self.weakenesses = ["grass"]


class Grass_Pokemon(Pokemon):
    def __init__(self, name, max_hp, attack, speed):
        super().__init__(name, max_hp, attack, speed)
        self.type = "fire"
        self.type_icon = "🍃"
        self.weakenesses = ["fire"]


class Psychic_Pokemon(Pokemon):
    def __init__(self, name, max_hp, attack, speed):
        super().__init__(name, max_hp, attack, speed)
        self.type = "psychic"
        self.type_icon = "🔮"
        self.weakenesses = ["psychic"]


pokemon_list = {
    "Gengar": {
        "name": "Gengar",
        "hp": 165,
        "attack": 75,
        "speed": 100,
        "type": "Psychic",
    },
    "Charizard": {
        "name": "Charizard",
        "hp": 200,
        "attack": 95,
        "speed": 75,
        "type": "Fire",
    },
    "Blastoise": {
        "name": "Blastoise",
        "hp": 190,
        "attack": 85,
        "speed": 70,
        "type": "Water",
    },
    "Venasaur": {
        "name": "Venasaur",
        "hp": 185,
        "attack": 80,
        "speed": 70,
        "type": "Grass",
    },
}


def build_pokemon_roster():
    # building a list of all possible pokemon to choose from this game
    pokemon_roster = {}
    for name, stats in pokemon_list.items():
        pokemon_roster[name] = globals()[f"{stats['type']}_Pokemon"](stats["name"], stats["hp"], stats["attack"], stats["speed"])
    return pokemon_roster


def list_pokemon_stats(roaster):
    print("------------------------------------- POKEMON STATS --------------------------------------\n ")
    for pokemon in roaster:
        selected = roaster[pokemon]
        # print(roaster[pokemon].current_hp)
        print(f"{1}) {selected.name} | HP: {selected.max_hp} | ATTACK: {selected.attack} | SPEED: {selected.speed} | TYPE {selected.type} {selected.type_icon}")
    print("\n------------------------------------------------------------------------------------------ ")
