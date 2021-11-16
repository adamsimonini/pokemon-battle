import random
from pokemon_pkg.choose import list_pokemon_to_user


class Trainer():
    def __init__(self, name):
        self.name = name
        self.pokemon_team = {}
        self.active_pokemon = None
        self.is_loser = False

    def get_name(self):
        return self.name

    def set_team(self, chosen_pokemon):
        self.pokemon_team = chosen_pokemon

    def get_team(self):
        return self.pokemon_team

    def get_active_pokemon(self):
        return self.active_pokemon

    def print_team_status(self):
        print(f"\n*** {self.name}'s current team status ***")
        for pokemon in self.pokemon_team:
            current_hp = getattr(self.pokemon_team[pokemon], "current_hp")
            max_hp = getattr(self.pokemon_team[pokemon], "max_hp")
            print(f"{self.name}'s {pokemon} has {current_hp}/{max_hp} HP")

    def select_active_pokemon(self):
        self.pokemon_team = filter_knocked_out(self.pokemon_team)
        pokemon_team = list(self.pokemon_team.keys())
        if len(pokemon_team) == 0:
            print(f"\n❌❌❌ {self.name} has had all their pokemon knocked out! ❌❌❌")
            return False
        if self.name == "Computer":
            selected_pokemon = random.choice(pokemon_team)
            self.active_pokemon = self.pokemon_team[selected_pokemon]
            pokemon = self.active_pokemon
            print(f"\nComputer has chosen {pokemon.type_icon}-{pokemon.name} as its active pokemon")
            return
        number_to_pokemon = list_pokemon_to_user(self.pokemon_team)
        players_choice = int(input("\nInput a number from the list above to select a pokemon. It will become your active pokemon: "))
        self.active_pokemon = self.pokemon_team[number_to_pokemon[players_choice]]


def filter_knocked_out(pokemon_team):
    remaining_team = {}
    for key in pokemon_team:
        pokemon = pokemon_team[key]
        if not pokemon.is_knocked_out:
            remaining_team[key] = pokemon
    return remaining_team
