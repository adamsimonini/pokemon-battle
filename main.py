import random
from user_pkg import user
from pokemon_pkg.pokemon import *
from setup import *

player = user.User("Player")
computer = user.User("Computer")


print(player.name)
print(computer.name)

pokemon_roster = []

# building a list of all possible pokemon to choose from this game
for name, stats in pokemon_list.items():
    # pokemon constructor: name, hp, attack, speed, type, weakness
    # add to pokemon_roster pokemon of class Pokemon using the pokemon_list for the data
    pokemon_roster.append(Pokemon(name, stats["hp"], stats["attack"], stats["speed"], stats["type"], stats["weakness"]))

# print(pokemon_roster[0])

# randomly select 3 pokemon for the computer
# print(computer.pokemon_team)
# print(choose_computers_team(pokemon_roster))
print("This is the computer's team before injecting pokemon: ")
computer.print_team()

# print("After injection: ")
computer.set_team(choose_computers_team(pokemon_roster))
player.set_team(choose_players_team(pokemon_roster))
# computer.pokemon_team.append(random.choices(pokemon_roster, k=3))


def print_pokemon_team(the_user):
    for players_pokemon in the_user.pokemon_team:
        print(players_pokemon.get_name())


print("\nCOMPUTER'S TEAM:")
print(computer.print_team())

print("\nUSER'S TEAM:")
print(player.print_team())

# print(pokemon_roster)
# load in pokemon
# assign two users
# enablue user to choose 3 pokemon
# randomly have computer choose 3 pokemon

# check if knockout, if so, check if win
