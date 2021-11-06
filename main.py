import random
from user_pkg import user
from pokemon_pkg import pokemon
from setup import choose_computers_team, choose_players_team

player = user.User("Player")
computer = user.User("Computer")

#  name, hp, attack, speed, type, weakness

print(player.name)
print(computer.name)

pokemon_roster = []

# building a list of all possible pokemon to choose from this game
for character in pokemon.pokemon_list:
    pokemon_roster.append(pokemon.Pokemon(character["name"], character["hp"], character["attack"], character["speed"], character["type"], character["weakness"]))
    # pokemon_roster_names.append(pokemon["name"])

# print(pokemon_roster[0])

# randomly select 3 pokemon for the computer
computer.pokemon_team = choose_computers_team(pokemon_roster)
player.pokemon_team = choose_players_team(pokemon_roster)
# computer.pokemon_team.append(random.choices(pokemon_roster, k=3))


def print_pokemon_team(the_user):
    for pokemon in the_user.pokemon_team:
        print(pokemon.get_name())


print("\nCOMPUTER'S TEAM:")
print(print_pokemon_team(computer))

print("\nUSER'S TEAM:")
print_pokemon_team(player)

# print(pokemon_roster)
# load in pokemon
# assign two users
# enablue user to choose 3 pokemon
# randomly have computer choose 3 pokemon

# check if knockout, if so, check if win
