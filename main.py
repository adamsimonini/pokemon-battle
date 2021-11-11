import random
import copy
import vlc
from user_pkg.user import *
from pokemon_pkg.pokemon import *
from pokemon_pkg.choose import *
from battle_pkg.battle import *

print('''_                              
            | |                             
 _ __   ___ | | _____ _ __ ___   ___  _ __  
| '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
| |_) | (_) |   <  __/ | | | | | (_) | | | |
| .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|
| |                                         
|_|     
''')

player = User("Player")
computer = User("Computer")

list_pokemon_stats()

# lOAD IN POKEMON
# creates a dictionary of Pokemon objects based on the pokemon within pokemon_list
pokemon_roster = build_pokemon_roster()

# deep copying pokemone rosters for each user, so they have their own unique Pokemon objects to choose from, and add to their team
computers_pokemon_roster = copy.deepcopy(pokemon_roster)
players_pokemon_roster = copy.deepcopy(pokemon_roster)

# SELECT POKEMON FOR THE COMPUTER
# randomly select 3 pokemon for the computer
computer.set_team(choose_computers_team(computers_pokemon_roster, 3))

# SELECT POKEMONE FOR THE PLAYER
player.set_team(choose_players_team(players_pokemon_roster))

computer.print_team_status()
player.print_team_status()

# BATTLE PHASE

# both users select their initial active pokemon
set_active_pokemon(computer)
set_active_pokemon(player)

# TODO: while neither player winner, battle
# battle_music = vlc.MediaPlayer("file:///audio/pokemon_battle-music.mp3")
# battle_music.play()
battle_turn(player, computer)
# battle_music.stop()

# assign two users
# enablue user to choose 3 pokemon
# randomly have computer choose 3 pokemon

# check if knockout, if so, check if win
