
import time
from Enemy import *
from Character import *


player_name = 'rem'
player_stats = [60, 15, 15, 15, 20]

player = Character(player_name, player_stats[0], player_stats[1],
                   player_stats[2], player_stats[3], player_stats[4])



def enemy_select(*args):
    enemy_list = [*args]
    length_list = (len(enemy_list))-1
    enemy_chance = random.randint(0, length_list)
    enemy = enemy_list[enemy_chance]
    return enemy

global enemy
enemy = enemy_select(orc, bat)

def display_enemy():
    if enemy.name.lower() == "orc":
        display_orc()
    elif enemy.name.lower() == "bat":
        display_bat()
    elif enemy.name.lower() == "skeleton":
        display_skeleton()
    else:
        print("Invisible monster has appeared!")

def enemy_attack():
    enemy_damage = enemy.get_attack() - player.defense
    enemy_crit_damage = enemy.get_critical_dmg()
    hit_crit_chance = round(random.uniform(0, 10), 2)

    if enemy.hit_chance > player.get_evade():
        if enemy.critical_chance > hit_crit_chance:

            if enemy_crit_damage <= 0:
                print(f"Nice! {player.name.title()} has invincible defense! {player.name.title()} takes 0 dmg!")

            else:
                player.health -= enemy_crit_damage
                print(f"{enemy.name.title()} deal critical {enemy_crit_damage} dmg! "
                      f"{player.name.title()} has {player.health}/{player.max_health} health.")
                return player.health

        elif enemy_damage <= 0:
                print(f"Nice! {player.name.title()} has invincible defense! {player.name.title()} takes 0 dmg!")

        else:
                player.health -= enemy_damage
                print(f"{enemy.name.title()} deal {enemy_damage} dmg. "
                      f"{player.name.title()} has {player.health}/{player.max_health} health.")
                return player.health
    else:
        print(f"{enemy.name.title()} miss")


def player_attack():

    player_damage = player.get_attack() - enemy.defense
    player_crit_damage = player.get_critical_dmg() - enemy.defense
    hit_miss_chance = round(random.uniform(0, 10), 2)
    hit_crit_chance = round(random.uniform(0, 10), 2)

    if player.hit_chance > hit_miss_chance:
        if player.get_critical() > hit_crit_chance:
            enemy.health -= player_crit_damage
            print(f"{player.name.title()} deal critical {player_crit_damage} dmg. "
                  f"{enemy.name.title()} has {enemy.health}/{enemy.max_health} health.")
            return enemy.health
        else:
            enemy.health -= player_damage
            print(f"{player.name.title()} deal {player_damage} dmg. "
                  f"{enemy.name.title()} has {enemy.health}/{enemy.max_health} health.")
            return enemy.health
    else:
        print(f"{player.name.title()} miss.")
        pass


def enemy_is_dead():
    orc_count = 0
    bat_count = 0
    skeleton_count = 0
    total_count = 0

    if enemy.health <= 0:
        print(f"{enemy.name} has been slayed. ")
        if enemy.name == "orc":
            orc_count += 1

        elif enemy.name == "bat":
            bat_count += 1

        elif enemy.name == "skeleton":
            skeleton_count += 1

        return enemy


    else:
        pass


def player_is_dead():
    time.sleep(0.7)
    if player.health <= 0:
        print("""



            ____    ____  ______    __    __      _______   __   _______  _______  
            \   \  /   / /  __  \  |  |  |  |    |       \ |  | |   ____||       \ 
             \   \/   / |  |  |  | |  |  |  |    |  .--.  ||  | |  |__   |  .--.  |
              \_    _/  |  |  |  | |  |  |  |    |  |  |  ||  | |   __|  |  |  |  |
                |  |    |  `--'  | |  `--'  |    |  '--'  ||  | |  |____ |  '--'  |
                |__|     \______/   \______/     |_______/ |__| |_______||_______/ 




            """)
        print("Your hero died but defeated {} orcs, {} bats, {} skeletons.")

    else:
        pass



def battle():



    while player.health > 0:
        player_attack()
        enemy_is_dead()
        enemy_attack()
        player_is_dead()




battle()