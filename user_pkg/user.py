class User():
    def __init__(self, name):
        self.name = name
        self.pokemon_team = []
        self.active_pokemon = None
        self.winner = False

    def set_team(self, chosen_pokemon):
        self.pokemon_team = chosen_pokemon

    def print_team(self):
        for character in self.pokemon_team:
            print(character.get_name())


