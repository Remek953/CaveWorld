
import time
from Enemy import *
from Character import *


player_name = 'rem'
player_stats = [40, 15, 5, 150, 20]

player = Character(player_name, player_stats[0], player_stats[1],
                   player_stats[2], player_stats[3], player_stats[4])


def enemy_select(*args):
    enemy_list = [*args]
    length_list = (len(enemy_list))-1
    enemy_chance = random.randint(0, length_list)
    enemy_1 = enemy_list[enemy_chance]
    return enemy_1


def attack(character, target):
    character_damage = character.get_attack() - target.defense
    character_crit_damage = character.get_critical_dmg() - target.defense
    hit_crit_chance = round(random.uniform(0, 10), 2)

    if character.get_hit_chance() > target.get_evade_chance():
        if character.get_critical_chance() > hit_crit_chance:

            if character_crit_damage <= 0:
                print(f"Nice! {target.name.title()} has invincible defense! {target.name.title()} takes 0 dmg!")

            else:
                target.health -= character_crit_damage
                print(f"{character.name.title()} deal critical {character_crit_damage} dmg! "
                      f"{target.name.title()} has {target.health}/{target.max_health} health.")
                return target.health

        elif character_damage <= 0:
                print(f"Nice! {target.name.title()} has invincible defense! {target.name.title()} takes 0 dmg!")

        else:
            target.health -= character_damage
            print(f"{character.name.title()} deal {character_damage} dmg. "
                  f"{target.name.title()} has {target.health}/{target.max_health} health.")
            return target.health
    else:
        print(f"{character.name.title()} miss")




def count():
    orc_count = 0
    bat_count = 0
    skeleton_count = 0
    total_count = 0

    if enemy.name.lower() == "orc":
        orc_count += 1


    elif enemy.name == "bat":
        bat_count += 1
        return bat_count

    elif enemy.name == "skeleton":
        skeleton_count += 1

    print(f"""
             Your hero died but defeated: 

             {orc_count} orcs, 
              bats, 
              skeletons.

         """)


def battle():

    global enemy
    enemy = enemy_select(Orc(), Bat())
    enemy.display()


    while player.health > 0:
        attack(player, enemy)
        if enemy.is_dead() is True:
            if battle() is None:
                break
        attack(enemy, player)
        player.is_dead()

print(player.max_health)

battle()
