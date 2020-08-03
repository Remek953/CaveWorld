import copy
import os
import random
import time


class Character:

    """
    Class represents the player character stats.
    """

    def __init__(self, name, strength, agility, dexterity, vitality, defense, race):

        self.name = name
        self.strength = strength
        self.agility = agility
        self.dexterity = dexterity
        self.max_health = round((100 + 5 * vitality), 2)
        self.health = round(self.max_health, 2)
        self.defense = defense
        self.base_attack = 20
        self.hit_chance = round(random.uniform(1, 10), 2)
        self.p_class = ""
        self.race = race

    def get_attack(self):

        attack = round(random.uniform((self.base_attack + self.strength) / 2, self.base_attack + self.strength))
        return attack

    def get_defense(self):

        defense = self.defense / 5
        return defense

    def get_hit_chance(self):

        return self.hit_chance + self.agility * 0.01

    def get_evade_chance(self):

        evade = round(random.uniform(0, 10), 2) + self.agility * 0.01
        return evade

    def get_critical_chance(self):

        critical = round(random.uniform(0, 10), 2) + self.dexterity * 0.01
        return critical

    def get_critical_dmg(self):

        critical_dmg = round(2 * self.get_attack(), 1)
        return critical_dmg

    def is_dead(self):

        if self.health <= 0:
            print("""
    ____    ____  ______    __    __      _______   __   _______  _______  
    \   \  /   / /  __  \  |  |  |  |    |       \ |  | |   ____||       \ 
     \   \/   / |  |  |  | |  |  |  |    |  .--.  ||  | |  |__   |  .--.  |
      \_    _/  |  |  |  | |  |  |  |    |  |  |  ||  | |   __|  |  |  |  |
        |  |    |  `--'  | |  `--'  |    |  '--'  ||  | |  |____ |  '--'  |
        |__|     \______/   \______/     |_______/ |__| |_______||_______/ 
        
                """)
            return True
        else:
            return False

    def warrior(self):

        self.p_class = "Warrior"
        self.strength = self.strength * 1.1
        self.defense = self.defense * 1.1

    def rogue(self):

        self.p_class = "Rogue"
        self.agility = self.agility * 1.1
        self.dexterity = self.dexterity * 1.1

    def monk(self):

        self.p_class = "Monk"
        self.max_health = round(self.max_health * 1.2, 2)


def create_name():

    name = input("What is your name:  ")
    while (len(name) < 1) and (len(name) > 12):
        print('Choose your name. Min 1 and max 12 characters')
        print("Username too short or too long")
        name = input("What is your name:  ")

    return name


def choose_race():

    print('''
|---------------------------------------------------------------------------|
|                        Choose your race:                                  |
|---------------------------------------------------------------------------|
|Human | 20 strength - 15 agility - 15 dexterity - 15 vitality - 15 defense |
|---------------------------------------------------------------------------|
|Orc   | 30 strength - 10 agility - 10 dexterity - 20 vitality - 20 defense |
|---------------------------------------------------------------------------|
|Elf   | 10 strength - 30 agility - 10 dexterity - 25 vitality - 15 defense |
|---------------------------------------------------------------------------|
|Fairy | 10 strength - 20 agility - 30 dexterity - 25 vitality - 15 defense |
|---------------------------------------------------------------------------|

            -------------------------------------------------
            |   Strength  - +1 min and max dmg              |
            -------------------------------------------------
            |   Agility   - +1% evade, +1% hit chance       |
            -------------------------------------------------
            |   Dexterity - +1% critical chance (2 x dmg)   |
            -------------------------------------------------
            |   Vitality  - +5 hitpoints                    |
            -------------------------------------------------
            |   Defense   - -0.2 dmg reduce                 |
            -------------------------------------------------
    
    ''')

    race = input("Enter race:  ")
    while race.lower() != 'human' and race.lower() != 'orc' and \
            race.lower() != 'elf' and race.lower() != 'fairy':
        print('\nPlease choose: Human or Orc or Elf or Fairy')
        race = input("Enter race:  ")

    race_stats = {}

    # Race stats
    while race_stats == {}:
        if race.lower() == "human":
            stats = {'strength': 20, 'agility': 15, 'dexterity': 15,
                     'vitality': 15, 'defense': 15, 'race': 'human'}
            race_stats.update(stats)

        elif race.lower() == 'orc':
            stats = {'strength': 30, 'agility': 10, 'dexterity': 10,
                     'vitality': 20, 'defense': 20, 'race': 'orc'}
            race_stats.update(stats)

        elif race.lower() == 'elf':
            stats = {'strength': 10, 'agility': 30, 'dexterity': 10,
                     'vitality': 25, 'defense': 15, 'race': 'elf'}
            race_stats.update(stats)

        elif race.lower() == 'fairy':
            stats = {'strength': 10, 'agility': 20, 'dexterity': 30,
                     'vitality': 20, 'defense': 10, 'race': 'fairy'}
            race_stats.update(stats)
    time.sleep(0.5)
    os.system("cls")

    return race_stats


def create_stats():

    time.sleep(0.5)
    os.system("cls")

    race_stats = choose_race()

    print("""
You have 100 points in a pool to spend as you wish on the attributes:

            -------------------------------------------------
            |   Strength  - +1 min and max dmg              |
            -------------------------------------------------
            |   Agility   - +1% evade, +1% hit chance       |
            -------------------------------------------------
            |   Dexterity - +1% critical chance (2 x dmg)   |
            -------------------------------------------------
            |   Vitality  - +5 hitpoints                    |
            -------------------------------------------------
            |   Defense   - -0.2 dmg reduce                 |
            -------------------------------------------------
        
If you choose to, you can then take points from an attribute and put them back in the pool.

        """)
    # Create a new independent copy of race stats
    attributes = copy.deepcopy(race_stats)

    # The amount of points to give away
    max_pool = 100
    pool = 100

    choice = None
    choice_sentence = """
        \n\nWhat would you like to do?
        1 - Spend points on an attribute
        2 - Put points into pool
        3 - Choose class
        """

    attribute_list = """
        \t - Strength
        \t - Agility
        \t - Dexterity
        \t - Vitality
        \t - Defense
        """

    while choice != "3":

        print(f"\nThere are {pool} points in the pool.")
        print(choice_sentence)

        choice = input("Choice: ")
        while choice != "1" and choice != "2" and choice != "3":
            print("Invalid choice")
            print(choice_sentence)
            choice = input("Choice: ")

        # Spend points on an attribute
        while choice == "1":
            # Pool of points is zero
            if pool == 0:
                print("Sorry, you don't have enough points.")
                break
            print(f"\nYou have {pool} points left in pool.")
            print("\nWhich attribute would you like to add to?")
            print(attribute_list)

            change_attributes = input("Attribute to change: ")
            while (
                   change_attributes.lower() != "strength" and
                   change_attributes.lower() != "agility" and
                   change_attributes.lower() != "dexterity" and
                   change_attributes.lower() != "vitality" and
                   change_attributes.lower() != "defense"
            ):
                print("That is an invalid choice.")
                print("Which attribute would you like to add to?")
                print(attribute_list)
                change_attributes = input("Attribute to change: ")
            else:
                points = int(input("How many points would you like to spend?: "))
                while points > pool:
                    print(f"That's too many points. You have {pool} to spend")
                    points = int(input("How many points would you like to spend?: "))

            attributes[change_attributes.lower()] += points
            pool -= points
            print("\nYour attributes")
            for attribute, points in attributes.items():
                print(f"\t{attribute.title()}:\t{points}")
            if pool == 0:
                print("\nYou've spent all your points.")
                choice = None
                break

            another_change = input("Want to change another attribute? Yes or No: ")
            while another_change.lower() != "yes" and another_change.lower() != "no" and \
                    another_change.lower() != "y" and another_change.lower() != "n":
                print("That's an invalid choice.")
                another_change = input("Want to change another attribute? Yes or No: ")
            if another_change.lower() == "no" or another_change.lower() == "n":
                break

        # Put points into pool
        while choice == "2":

            # Pool already full
            if pool == max_pool:
                print("\nSorry, you have no points in your attributes."
                      "\nTry adding some points to your attributes first.")
                break

            print("\nWhich attribute would you like to take points out of?")
            for attribute, points in attributes.items():
                print(f"\t{attribute.title()}:  \t{points}")
            change_attributes = input("Choice: ")
            while (
                    change_attributes.lower() != "strength" and
                    change_attributes.lower() != "agility" and
                    change_attributes.lower() != "dexterity" and
                    change_attributes.lower() != "vitality" and
                    change_attributes.lower() != "defense"
            ):
                print("\nThat is an invalid choice.")
                print("\nWhich attribute would you like to take points out of?")
                for attribute, points in attributes.items():
                    print(f"\t{attribute.title()}:  \t{points}")
                change_attributes = input("Choice: ")

            # Pool of points is zero
            while attributes[change_attributes.lower()] == 0:

                print("You don't have any points in that attribute.")
                change_attributes = input("Choice: ")

                while (
                        change_attributes.lower() != "strength" and
                        change_attributes.lower() != "agility" and
                        change_attributes.lower() != "dexterity" and
                        change_attributes.lower() != "vitality" and
                        change_attributes.lower() != "defense"
                ):
                    print("That is an invalid choice.")
                    print("Which attribute would you like to take points out of?")
                    change_attributes = input("Choice: ")
            points = int(input("\nHow many points would you like to remove?: "))

            # Not enough points in attribute
            while points > attributes[change_attributes.lower()]:

                print(f"Sorry, that's too many points! You only have {attributes[change_attributes.lower()]} "
                      f"in {change_attributes.lower()} ")
                points = int(input("\nHow many points would you like to remove?: "))

            check_stats = attributes[change_attributes.lower()] - points

            # Cant change constant value in race_stats
            while check_stats < race_stats[change_attributes.lower()]:

                print(f"Sorry, You cant change basic race stats. Your race stat is "
                      f"{race_stats[change_attributes.lower()]} in {change_attributes.lower()}.")
                points = 0
                choice = '2'
                break

            # Continue change another attribute
            another_change = input("\nWant to change another attribute? Yes or No: ")
            while another_change.lower() != "yes" and another_change.lower() != "no" \
                    and another_change.lower() != "y" and another_change.lower() != "n":
                print("That's an invalid choice.")
                another_change = input("Want to change another attribute? Yes or No: ")
            if another_change.lower() == "no" or another_change.lower() == "n":
                choice = None
                break

            print("Alright!")
            pool += points
            attributes[change_attributes.lower()] -= points
            print(f"You now have {pool} points left in your pool.")

    return attributes['strength'], attributes['agility'], attributes['dexterity'], \
           attributes['vitality'], attributes['defense'], race_stats['race']


def choose_class():

    time.sleep(0.5)
    os.system("cls")

    print("""
              Choose your class:
----------------------------------------------------- 

             /'
             ||
             ||      ** *
             ||      __X_
             ||     ( ___\\
             ||     |:  \\\\
            ><><  ___)..:/_#__,
            (X|) (|+(____)+\ _)
             o|_\/>> + + + << \\
               |:\/|+ + + +| \_\<
               \./  XXXXXX.  (o_)_
                   /+ + + |   \:|  b'ger

    1 - Warrior - +10% strength
                  +10% defence
    
-----------------------------------------------------     
   
                    |  |
                    |--|
                    |  |
                  _.+  +._
                 /\,)    /\\
                :  `-._.'  ;
                |      "*--|
                | \        |
                |  `.      ;
                :         /|
                |\      -' | bug
                    
   
    2 - Rogue - +10% evade 
                +10% hit chance 
                +10% critical chance
    
-----------------------------------------------------  
                   ___
                 //|||\\\\
                 /|^,^|\\\\
                 ||\-/|||    
                 \\\\| ||||    
                /|-----|\\
               |\|  &  |/|
               | |     | |
               | |     | |   Ramon Herrera


    3 - Monk - +20% max health
    
-----------------------------------------------------    
    """)

    char_class = input("What is your characters class:  ")

    while True:
        if char_class == '1' or char_class.lower() == 'warrior':

            return player.warrior()

        elif char_class == '2' or char_class.lower() == 'rogue':

            return player.rogue()

        elif char_class == '3' or char_class.lower() == 'monk':

            return player.monk()

        else:

            char_class = input("What is your characters class:  ")


# Assign a name, race and stats to the player
def create_character():

    global player

    player_name = create_name()
    player_stats = create_stats()
    player = Character(player_name, player_stats[0], player_stats[1],
                       player_stats[2], player_stats[3], player_stats[4], player_stats[5])
    choose_class()

    return player

