import random
import copy
from user_pkg import user
from pokemon_pkg.pokemon import *
from choose_pokemon import *

print('''_                              
            | |                             
 _ __   ___ | | _____ _ __ ___   ___  _ __  
| '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
| |_) | (_) |   <  __/ | | | | | (_) | | | |
| .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|
| |                                         
|_|     
''')

player = user.User("Player")
computer = user.User("Computer")

# creates a dictionary of Pokemon objects based on the pokemon within pokemon_list
pokemon_roster = build_pokemon_roster()

# deep copying pokemone rosters for each user, so they have their own unique Pokemon objects to choose from, and add to their team
computers_pokemon_roster = copy.deepcopy(pokemon_roster)
players_pokemon_roster = copy.deepcopy(pokemon_roster)

# randomly select 3 pokemon for the computer
# print(computer.pokemon_team)
# print(choose_computers_team(pokemon_roster))
# print("This is the computer's team before injecting pokemon: ")
# computer.print_team()

computer.set_team(choose_computers_team(computers_pokemon_roster, 3))
print("COMPUTER'S TEAM:")
print(computer.get_team())

player.set_team(choose_players_team(players_pokemon_roster))
print("PLAYER'S TEAM:")
print(player.get_team())

computer.print_team_status()

# def print_pokemon_team(the_user):
#     for players_pokemon in the_user.pokemon_team:
#         print(players_pokemon.get_name())

# print("\nCOMPUTER'S TEAM:")
# print(computer.print_team())

# print("\nUSER'S TEAM:")
# print(player.print_team())

# print(pokemon_roster)
# load in pokemon
# assign two users
# enablue user to choose 3 pokemon
# randomly have computer choose 3 pokemon

# check if knockout, if so, check if win
