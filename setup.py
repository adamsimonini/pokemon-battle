import random


def choose_computers_team(pokemon):
    team = random.choices(pokemon, k=3)
    return team


def list_pokemon_to_user(list):
    print("")
    for i, pokemon in enumerate(list):
        print(f"{i + 1}: {pokemon.get_name()}")


def choose_players_team(pokemon_list):
    chosen_pokemon = []
    players_choice = 0
    for n in range(3):
        print(f"Now choosing {n + 1}/3 pokemon to add to your team:")
        # show player a list of pokemon to choose from

        list_pokemon_to_user(pokemon_list)

        # have player choose a pokemon
        while players_choice < 1 or players_choice > len(pokemon_list):
            players_choice = int(input("\nInput a number to select a pokemon from the list above: "))
            if players_choice in range(1, len(pokemon_list), 1):
                chosen_pokemon.append(pokemon_list[players_choice - 1])
                print(f"\n{pokemon_list[players_choice].get_name()} has been added to your team!")
                continue
            else:
                print(f"Your selection was invalid. Please choose a number between 1 and {len(pokemon_list)}")
                list_pokemon_to_user(pokemon_list)
    return chosen_pokemon
