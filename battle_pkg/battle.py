import random
import time


def attack(attacker, defender):
    time.sleep(1.2)
    attackers_pokemon = attacker.active_pokemon
    defenders_pokemon = defender.active_pokemon
    attack_damage = attackers_pokemon.attack

    # remaining_hp = (opponent.get_current_hp()) - (attacker.get_attack())
    if attackers_pokemon.type in defenders_pokemon.weaknesses:
        attack_damage = attack_damage * 1.5
        print(f"\n{attackers_pokemon.name}'s attack is super effective!")
        defenders_pokemon.current_hp = defenders_pokemon.current_hp - attack_damage
    else:
        defenders_pokemon.current_hp = defenders_pokemon.current_hp - attackers_pokemon.attack

    print(f"\n{attacker.name}'s {attackers_pokemon.type_icon}-{attackers_pokemon.name}-🗡️  attacks {defender.name}'s {defenders_pokemon.type_icon}-{defenders_pokemon.name}-🛡️  for {attack_damage} damage!")

    if defenders_pokemon.current_hp < 1:
        defenders_pokemon.is_knocked_out = True
        return False

    print(f"{defender.name}'s {defenders_pokemon.name} has {defenders_pokemon.current_hp}/{defenders_pokemon.max_hp} HP remaining...")


def decide_attack_order(user_one, user_two):
    user_one_active_pokemon = user_one.active_pokemon
    user_two_active_pokemon = user_two.active_pokemon
    if user_one_active_pokemon.speed > user_two_active_pokemon.speed:
        return [user_one, user_two]
    elif user_one_active_pokemon.speed < user_two_active_pokemon.speed:
        return [user_two, user_one]
    else:
        return random.sample([user_one, user_two], 2)


def battle(user_one, user_two):
    # resolve speed to see which user goes first
    first, second = decide_attack_order(user_one, user_two)

    first_active_pokemon = first.active_pokemon
    second_active_pokemon = second.active_pokemon

    print(f"*** {first.name}'s {first_active_pokemon.name} attacks first, and then {second.name}'s {second_active_pokemon.name} will attack if it survives ***")
    while not first_active_pokemon.is_knocked_out and not second_active_pokemon.is_knocked_out:

        attack(first, second)
        if check_for_knockout(second):
            break

        attack(second, first)
        if check_for_knockout(first):
            break


def check_for_knockout(user):
    active_pokemon = user.active_pokemon
    if active_pokemon.is_knocked_out:
        print(f"\n{user.name}'s {active_pokemon.type_icon}-{active_pokemon.name}-💀 has been knocked out!")
        if user.select_active_pokemon() == False:
            user.is_loser = True
            declare_winner(user)
    return False


def declare_winner(user):
    if user.name == "Computer":
        print(f"\n***** {user.name} has lost the game! *****")
        print("***** Congratulations! You win! 🥳 *****")
        exit()
    print(f"\n***** {user.name} has lost the game! *****")
    print("***** You lose. Better luck next time trainer! 😭 *****")
    exit()
