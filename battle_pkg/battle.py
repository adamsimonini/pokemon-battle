import random
import time

# def set_active_pokemon(user):
#     # filter out knocked out pokemon form user's team
#     possible_pokemon = filter(filter_knocked_out, user.pokemon_team)
#     # for pokemon in possible_pokemon:
#     #     print(pokemon["name"])
#     print(possible_pokemon)


def set_active_pokemon(user):
    if user == "Computer":
        user.select_active_pokemon()
        # print(f"\nComputer's Active Pokemon: {user.active_pokemon.get_type_icon()} {user.active_pokemon.get_hp_status()}")

    user.select_active_pokemon()
    # print(f"\n{user.get_name()}'s Active Pokemon: {user.active_pokemon.get_type_icon()} {user.active_pokemon.get_hp_status()}")


def filter_knocked_out(pokemon):
    print(pokemon)
    if pokemon["knocked_out"]:
        return False
    else:
        return True


def attack(attacker, defender):
    time.sleep(1.2)
    attackers_pokemon = attacker.active_pokemon
    defenders_pokemon = defender.active_pokemon

    print(f"\n{attacker.name}'s {attackers_pokemon.type_icon}-{attackers_pokemon.name}-🗡️  attacks {defender.name}'s {defenders_pokemon.type_icon}-{defenders_pokemon.name}-🛡️  for {attackers_pokemon.attack} damage!")
    # remaining_hp = (opponent.get_current_hp()) - (attacker.get_attack())
    defenders_pokemon.current_hp = defenders_pokemon.current_hp - attackers_pokemon.attack
    if defenders_pokemon.current_hp < 1:
        defenders_pokemon.is_knocked_out = True
        return False

    print(f"{defender.name}'s {defenders_pokemon.name} has {defenders_pokemon.current_hp}/{defenders_pokemon.max_hp} HP remaining...")


def decide_attack_order(user_one, user_two):
    user_one_active_pokemon = user_one.active_pokemon
    user_two_active_pokemon = user_two.active_pokemon
    if user_one_active_pokemon.get_speed() > user_two_active_pokemon.get_speed():
        return [user_one, user_two]
    elif user_one_active_pokemon.get_speed() < user_two_active_pokemon.get_speed():
        return [user_two, user_one]
    else:
        print(random.sample([user_one, user_two], 2))
        return random.sample([user_one, user_two], 2)


def battle_turn(user_one, user_two):
    print("\n------------------------------------- BATTLE --------------------------------------\n ")
    # resolve speed to see which user goes first
    first, second = decide_attack_order(user_one, user_two)

    first_active_pokemon = first.active_pokemon
    second_active_pokemon = second.active_pokemon

    print(f"{first.name}'s {first_active_pokemon.name} attacks first, and then {second.name}'s {second_active_pokemon.name} will attack if it survives")
    while not first_active_pokemon.is_knocked_out and not second_active_pokemon.is_knocked_out:

        # print(f"\n*** {first.name}'s {first_active_pokemon.name}🗡️  attacks {second.name}'s {second_active_pokemon.name}🛡️ ***")
        attack(first, second)
        if check_for_knockout(second, second_active_pokemon):
            break

        attack(second, first)
        if check_for_knockout(first, first_active_pokemon):
            break


def check_for_knockout(user, pokemon):
    if pokemon.is_knocked_out:
        print(f"\n{user.name}'s {pokemon.type_icon}-{pokemon.name}💀 has been knocked out!")
        return True
    return False
