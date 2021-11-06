class User():
    def __init__(self, name):
        self.name = name
        self.pokemon_team = []
        self.active_pokemon = None
        self.winner = False

    def set_team(self, chosen_pokemon):
        self.pokemon_team = chosen_pokemon
