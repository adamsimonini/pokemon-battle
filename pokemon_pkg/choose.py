import random
from pokemon_pkg.pokemon import type_icons


def choose_computers_team(pokemon_roster, team_size):
    computers_team = {}
    for i in range(team_size):
        random_pokemon = random.choice(list(pokemon_roster))
        computers_team[random_pokemon] = pokemon_roster[random_pokemon]
        pokemon_roster.pop(random_pokemon, None)
    return computers_team


def list_pokemon_to_user(pokemon_roster):
    number_to_pokemon = {}
    print("")
    for i, pokemon_name in enumerate(pokemon_roster):
        print(f"{i + 1}: {pokemon_name} {pokemon_roster[pokemon_name].get_type_icon()}")
        number_to_pokemon[i + 1] = pokemon_name
    return number_to_pokemon


def choose_players_team(pokemon_roster):
    chosen_pokemon = {}
    turn_number = 1
    while len(chosen_pokemon) < 3:
        print(f"\nNow choosing spot {turn_number} of 3 for your pokemon team:")
        number_to_pokemon = list_pokemon_to_user(pokemon_roster)
        players_choice = int(input("\nInput a number to select a pokemon from the list above: "))
        # range end is not inclusive, hence the +1
        if players_choice > 0 and players_choice in range(len(pokemon_roster) + 1):
            pokemon = pokemon_roster[number_to_pokemon[players_choice]]
            chosen_pokemon[pokemon.get_name()] = pokemon
            print(f"\n*** {pokemon.get_name()} {pokemon.get_type_icon()} has been added to your team! ***")
            pokemon_roster.pop(pokemon.get_name(), None)
            turn_number += 1
            continue

        print(f"Your selection was invalid. Please choose a number between 1 and {len(pokemon_roster)}")

        # reset players_choice so we enter the while loop on next iteration
    return chosen_pokemon
