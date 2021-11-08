class User():
    def __init__(self, name):
        self.name = name
        self.pokemon_team = {}
        self.active_pokemon = None
        self.winner = False

    def set_team(self, chosen_pokemon):
        self.pokemon_team = chosen_pokemon

    # def get_team(self):
    #     for pokemon in self.pokemon_team:
    #         print(pokemon["name"])

    def get_team(self):
        return self.pokemon_team

    def print_team_status(self):
        print(f"\n*** {self.name}'s current team status ***")
        for pokemon in self.pokemon_team:
            current_hp = getattr(self.pokemon_team[pokemon], "current_hp")
            max_hp = getattr(self.pokemon_team[pokemon], "max_hp")
            print(f"{self.name}'s {pokemon} has {current_hp}/{max_hp} HP")
