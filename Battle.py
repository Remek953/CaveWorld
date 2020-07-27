from Enemy import *
from Character import *


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


class PointsAndKillCounts():
    def __init__(self, orc_kills=0, bat_kills=0, skeleton_kills=0, orc_points=0, bat_points=0, skeleton_points=0, total_points=0):
        self.orc_kills = orc_kills
        self.bat_kills = bat_kills
        self.skeleton_kills = skeleton_kills
        self.orc_points = orc_points
        self.bat_points = bat_points
        self.skeleton_points = skeleton_points
        self.total_points = total_points

    def result(self, player):
        print(f"""
        {player.name.title()} defeated: 
        - {self.orc_kills} orcs!
        - {self.bat_kills} bats!
        - {self.skeleton_kills} skeletons!

        {player.name.title()} defetead:
        - {self.orc_points} points from orcs,
        - {self.bat_points} points from bats,
        - {self.skeleton_points} points from skeletons. 

        TOTAL: {self.total_points} points! 

        Good luck next time!

        """)

        self.orc_kills = 0
        self.bat_kills = 0
        self.skeleton_kills = 0
        self.orc_points = 0
        self.bat_points = 0
        self.skeleton_points = 0
        self.total_points = 0


def count():
    if enemy.name.lower() == "orc":
        points.orc_kills += 1
        points.orc_points += enemy.points
        points.total_points += enemy.points

    elif enemy.name.lower() == "bat":
        points.bat_kills += 1
        points.bat_points += enemy.points
        points.total_points += enemy.points

    elif enemy.name.lower() == "skeleton":
        points.skeleton_kills += 1
        points.skeleton_points += enemy.points
        points.total_points += enemy.points

    else:
        print("You defeated monster")


points = PointsAndKillCounts()
def battle(player):

    global enemy
    enemy = enemy_select(Orc(), Bat(), Skeleton())
    enemy.display()

    while player.health > 0:
        attack(player, enemy)
        if enemy.is_dead() is True:
            count()
            return battle(player)
        attack(enemy, player)
        if player.is_dead() is True:
            points.result(player)


