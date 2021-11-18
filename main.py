import copy
import vlc
from trainer_pkg.trainer import *
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

player = Trainer("Player")
computer = Trainer("Computer")

# lOAD IN POKEMON
# creates a dictionary of Pokemon objects based on the pokemon within pokemon_list
pokemon_roster = build_pokemon_roster()

list_pokemon_stats(pokemon_roster)
# deep copying pokemone rosters for each user, so they have their own unique Pokemon objects to choose from, and add to their team
computers_pokemon_roster = copy.deepcopy(pokemon_roster)
players_pokemon_roster = copy.deepcopy(pokemon_roster)

# SELECT POKEMON FOR THE COMPUTER
computer.set_team(choose_computers_team(computers_pokemon_roster, 3))

# SELECT POKEMONE FOR THE PLAYER
player.set_team(choose_players_team(players_pokemon_roster))

# BATTLE PHASE

# both users select their initial active pokemon
player.select_active_pokemon()
computer.select_active_pokemon()

print("\n------------------------------------- BATTLE --------------------------------------\n ")
# battle_music = vlc.MediaPlayer("file:///audio/pokemon_battle-music.mp3")
# battle_music.play()

while player.is_loser == False and computer.is_loser == False:
    battle(player, computer)

# battle_music.stop()
