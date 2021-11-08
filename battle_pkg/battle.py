# def set_active_pokemon(user):
#     # filter out knocked out pokemon form user's team
#     possible_pokemon = filter(filter_knocked_out, user.pokemon_team)
#     # for pokemon in possible_pokemon:
#     #     print(pokemon["name"])
#     print(possible_pokemon)


def initial_active_pokemon(player, computer):
    player.select_active_pokemon()
    print(f"\n{player.get_name()}'s Active Pokemon:")
    print(player.active_pokemon.get_name(), player.active_pokemon.get_type_icon(), player.active_pokemon.get_hp_status())

    computer.select_active_pokemon()
    print("\nComputer's Active Pokemon:")
    print(computer.active_pokemon.get_name(), computer.active_pokemon.get_type_icon(), computer.active_pokemon.get_hp_status())

def filter_knocked_out(pokemon):
    print(pokemon)
    if pokemon["knocked_out"]:
        return False
    else:
        return True
