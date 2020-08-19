from Enemy import *
from Character import *
import csv


def battle_intro():

    clear_screen()

    """ 3 different random intros to the game """

    b_intro = random.randint(1, 3)

    if b_intro == 1:

        print('''
        
                         ______________
                   ,===:'.,            `-._
                        `:.`---.__         `-._
                          `:.     `--.         `.
                            \.        `.         `.
                    (,,(,    \.         `.   ____,-`.,
                 (,'     `/   \.   ,--.___`.'
             ,  ,'  ,--.  `,   \.;'         `
              `{D, {    \  :    \;
                V,,'    /  /    //
                j;;    /  ,' ,-//.    ,---.      ,
                \;'   /  ,' /  _  \  /  _  \   ,'/
                      \   `'  / \  `'  / \  `.' /
                       `.___,'   `.__,'   `.__,'  John VanderZwaag
            
            ------------------------------------------------
            This ASCII pic can be found at
            https://asciiart.website/index.php?art=creatures/dragons


The world is in chaos and no one can stop you from gain glory and fame.
Use your magnificent and innate skills to kill as many monsters as possible.

Good Luck!


        ''')
        time.sleep(5)
        clear_screen()

    elif b_intro == 2:

        print('''
        #####################################################
        #######_#########################################DWB#
        ######/ \#####_________######_______#################
        #####|\ /|###(_________)####(_______)###_____###__###
        #####| V |###|  |###|  |####|  \#/  |##(_____)#(__)##
        #####| | |___|   |##|  |_###|   |   |#|  \#/ |#\  |##
        ###__| | |___|   |##|  | |##|   |   |#|  |#| |#|  |##
        ##(__| | | V_|   |##|  | |##|   |   ||   |#| |#|  |##
        ##||#| | |_/_|    |/   | |#|    |   ||   ||  |#|  |##
        ##||#| | |###|    /    |###|    |   |    |   |#|  |##
        `````````````````````````````````````````````````````
        
        
        ------------------------------------------------
        This ASCII pic can be found at
        https://asciiart.website/index.php?art=places/stonehenge

15 years ago, the first “dungeon” that connected the real world with the monster world opened.
People received the power to hunt monsters within the dungeon. 
They are known as "Adventurers".
Enter the first "A+" level dungeon: CaveWorld.
Find the legendary sword and save the world from monsters.

Good Luck!

        ''')
        time.sleep(5)
        clear_screen()

    elif b_intro == 3:

        print('''
        
                                  ================================
                   /__\            ||     ||<(.)>||<(.)>||     ||
       ____________|  |            ||    _||     ||     ||_    ||
       |_|_|_|_|_|_|  |            ||   (__D     ||     C__)   ||
       |_|_|_|_|_|_|__|            ||   (__D     ||     C__)   ||
      A@\|_|_|_|_|_|/@@Aa          ||   (__D     ||     C__)   ||
   aaA@@@@@@@@@@@@@@@@@@@aaaA      ||   (__D     ||     C__)   ||
  A@@@@@@@@@@@DWB@@@@@@@@@@@@A     ||     ||     ||     ||  dwb||
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  ================================

        ------------------------------------------------
        This ASCII pic can be found at
        https://asciiart.website/index.php?art=places/alcatraz


You was wrongly accused of murder. You have been sent to The CaveWorld. 
The most dangerous prison on the world. 
You will spend the rest of your life in that place. 
Escape from prison and prove your innocent.

Good Luck!
        
        ''')
        time.sleep(5)
        clear_screen()


# Enemy select from list of monsters
def enemy_select(*args):

    enemy_list = [*args]
    length_list = (len(enemy_list))-1
    enemy_chance = random.randint(0, length_list)
    enemy_1 = enemy_list[enemy_chance]
    return enemy_1


# Battle system
def attack(character, target):

    character_damage = character.get_attack() - target.get_defense()
    character_crit_damage = character.get_critical_dmg() - target.get_defense()
    hit_crit_chance = round(random.uniform(0, 10), 2)

    if character.get_hit_chance() > target.get_evade_chance():
        if character.get_critical_chance() > hit_crit_chance:

            if character_crit_damage <= 0:
                print(f"Nice! {target.name.title()} has invincible defense! {target.name.title()} takes 0 dmg!")

            else:
                target.health -= character_crit_damage
                print(f"{character.name.title()} deal critical {round(character_crit_damage)} dmg! "
                      f"{target.name.title()} has {round(target.health)}/{target.max_health} health.")
                return target.health

        elif character_damage <= 0:
            print(f"Nice! {target.name.title()} has invincible defense! {target.name.title()} takes 0 dmg!")

        else:
            target.health -= character_damage
            print(f"{character.name.title()} deal {round(character_damage)} dmg. "
                  f"{target.name.title()} has {round(target.health)}/{target.max_health} health.")
            return target.health
    else:
        print(f"{character.name.title()} takes huge swing and miss!")


# Scoreboard: kills and points from monsters
class Scoreboard:

    def __init__(self, orc_kills=0, bat_kills=0, skeleton_kills=0, ant_kills=0, scorpion_kills=0, total_kills=0,
                 orc_points=0, bat_points=0, skeleton_points=0, ant_points=0, scorpion_points=0, total_points=0,):

        self.orc_kills = orc_kills
        self.bat_kills = bat_kills
        self.skeleton_kills = skeleton_kills
        self.ant_kills = ant_kills
        self.scorpion_kills = scorpion_kills

        self.total_kills = total_kills

        self.orc_points = orc_points
        self.bat_points = bat_points
        self.skeleton_points = skeleton_points
        self.ant_points = ant_points
        self.scorpion_points = scorpion_points

        self.total_points = total_points

    def reset(self):

        self.orc_kills = 0
        self.bat_kills = 0
        self.skeleton_kills = 0
        self.ant_kills = 0
        self.scorpion_kills = 0

        self.total_kills = 0

        self.orc_points = 0
        self.bat_points = 0
        self.skeleton_points = 0
        self.ant_points = 0
        self.scorpion_points = 0

        self.total_points = 0

    def result(self, player):

        print(f"""
{player.name.title()} defeated: 
- {self.orc_kills} orcs,
- {self.bat_kills} bats,
- {self.skeleton_kills} skeletons,
- {self.ant_kills} ants,
- {self.scorpion_kills} scorpions.

{player.name.title()} defeated {self.total_kills} monsters!

{player.name.title()} received:
- {self.orc_points} points from orcs,
- {self.bat_points} points from bats,
- {self.skeleton_points} points from skeletons. 
- {self.ant_points} points from ants. 
- {self.scorpion_points} points from scorpions. 

{player.name.title()} has {self.total_points} points! 

Good luck next time!

        """)


# Kills and points count
def count():

    if enemy.name.lower() == Orc().name.lower():
        points.orc_kills += 1
        points.total_kills += 1
        points.orc_points += enemy.points
        points.total_points += enemy.points

    elif enemy.name.lower() == Bat().name.lower():
        points.bat_kills += 1
        points.total_kills += 1
        points.bat_points += enemy.points
        points.total_points += enemy.points

    elif enemy.name.lower() == Skeleton().name.lower():
        points.skeleton_kills += 1
        points.total_kills += 1
        points.skeleton_points += enemy.points
        points.total_points += enemy.points

    elif enemy.name.lower() == Ant().name.lower():
        points.ant_kills += 1
        points.total_kills += 1
        points.ant_points += enemy.points
        points.total_points += enemy.points

    elif enemy.name.lower() == Scorpion().name.lower():
        points.scorpion_kills += 1
        points.total_kills += 1
        points.scorpion_points += enemy.points
        points.total_points += enemy.points

    else:
        print("You defeated monster")


# Assignment scoreboard to variable
points = Scoreboard()


# Save scores to Scores.csv
def save_scores(player):

    with open("Scores.csv", "a", newline="") as file_object:
        fieldnames = ["Name", "Race", "Class", "Kills", "Points"]
        csv_writer = csv.DictWriter(file_object, fieldnames=fieldnames)

        csv_writer.writerow({"Name": player.name, "Race": player.race, "Class": player.p_class,
                             "Kills": points.total_kills, "Points": points.total_points})


def battle(player):

    time.sleep(0.5)
    clear_screen()

    global enemy
    # Enemy select from Enemy.py
    enemy = enemy_select(Orc(), Bat(), Skeleton(), Ant(), Scorpion())
    enemy.display()

    while player.health > 0:

        attack(player, enemy)
        time.sleep(0.3)
        if enemy.is_dead() is True:
            count()
            return battle(player)

        attack(enemy, player)
        time.sleep(0.3)
        print("\n")
        if player.is_dead() is True:
            time.sleep(2)
            clear_screen()
            points.result(player)
            time.sleep(6)
            save_scores(player)
            points.reset()
            clear_screen()


