import random
from pokemon_pkg.choose import list_pokemon_to_user


class User():
    def __init__(self, name):
        self.name = name
        self.pokemon_team = {}
        self.active_pokemon = None
        self.winner = False

    def get_name(self):
        return self.name

    def set_team(self, chosen_pokemon):
        self.pokemon_team = chosen_pokemon

    def get_team(self):
        return self.pokemon_team

    def print_team_status(self):
        print(f"\n*** {self.name}'s current team status ***")
        for pokemon in self.pokemon_team:
            current_hp = getattr(self.pokemon_team[pokemon], "current_hp")
            max_hp = getattr(self.pokemon_team[pokemon], "max_hp")
            print(f"{self.name}'s {pokemon} has {current_hp}/{max_hp} HP")

    def select_active_pokemon(self):
        pokemon_team = list(self.pokemon_team.keys())
        if self.name == "Computer":
            selected_pokemon = random.choice(pokemon_team)
            self.active_pokemon = self.pokemon_team[selected_pokemon]
            return None
        number_to_pokemon = list_pokemon_to_user(self.pokemon_team)
        players_choice = int(input("\nInput a number from the list above to select a pokemon. It will become your active pokemon: "))
        self.active_pokemon = self.pokemon_team[number_to_pokemon[players_choice]]
