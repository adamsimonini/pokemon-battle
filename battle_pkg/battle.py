import random
# def set_active_pokemon(user):
#     # filter out knocked out pokemon form user's team
#     possible_pokemon = filter(filter_knocked_out, user.pokemon_team)
#     # for pokemon in possible_pokemon:
#     #     print(pokemon["name"])
#     print(possible_pokemon)


def set_active_pokemon(user):
    if user == "Computer":
        user.select_active_pokemon()
        print(f"\nComputer's Active Pokemon: {user.active_pokemon.get_type_icon()} {user.active_pokemon.get_hp_status()}")

    user.select_active_pokemon()
    print(f"\n{user.get_name()}'s Active Pokemon: {user.active_pokemon.get_type_icon()} {user.active_pokemon.get_hp_status()}")


def filter_knocked_out(pokemon):
    print(pokemon)
    if pokemon["knocked_out"]:
        return False
    else:
        return True


def attack(attacker, defender):
    # remaining_hp = (opponent.get_current_hp()) - (attacker.get_attack())
    defender.set_hp((defender.get_current_hp()) - (attacker.get_attack()))


def decide_attack_order(user_one, user_two):
    user_one_active_pokemon = user_one.get_active_pokemon()
    user_two_active_pokemon = user_two.get_active_pokemon()
    if user_one_active_pokemon.get_speed() > user_two_active_pokemon.get_speed():
        return [user_one, user_two]
    elif user_one_active_pokemon.get_speed() < user_two_active_pokemon.get_speed():
        return [user_two, user_one]
    else:
        print(random.sample([user_one, user_two], 2))
        return random.sample([user_one, user_two], 2)


def battle_turn(user_one, user_two):
    # resolve speed to see which user goes first
    first, second = decide_attack_order(user_one, user_two)

    first_active_pokemon = first.get_active_pokemon()
    second_active_pokemon = second.get_active_pokemon()

    print(f"{first.get_name()}'s {first_active_pokemon.get_name()} attacks first, and then {second.get_name()}'s {second_active_pokemon.get_name()} will attack if it survives")

    attack(first_active_pokemon, second_active_pokemon)

    print(second_active_pokemon.get_hp_status())

    if second_active_pokemon.get_knocked_out_status():
        # force a switch of pokemon
        return False

    attack(second_active_pokemon, first_active_pokemon)

    print(first_active_pokemon.get_hp_status())
