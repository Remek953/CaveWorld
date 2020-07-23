import copy
import os
import random

class Character:
    def __init__(self, name, strength, agility, luck, health, defense):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.max_health = 100 + 5*health
        self.health = self.max_health
        self.defense = defense
        self.base_attack = 20
        self.critical_chance = 2
        self.hit_chance = 8

    def get_attack(self):
        attack = round(random.uniform((self.base_attack + self.strength) / 2,
                                         self.base_attack + self.strength))
        return attack

    def get_evade(self):
        evade = round(random.uniform(0, 10), 2) + self.agility * 0.01
        return evade

    def get_critical(self):
        critical = round(random.uniform(0, 10), 2) + self.luck * 0.01
        return critical

    def get_critical_dmg(self):
        critical_dmg = 2 * self.get_attack()
        return critical_dmg











def create_name():
    name = input("What is your name:  ")
    while (len(name) < 1) and (len(name) > 12):
        print('Choose your name. Min 1 and max 12 characters')
        print("Username too short or too long")
        name = input("What is your name:  ")
    return name


def choose_race():
    print('''Choose your race: 
    Human -  \t20 strength \t15 agility \t15 luck \t15 health \t15 defense
    Orc -    \t30 strength \t10 agility \t10 luck \t20 health \t20 defense
    Elf -    \t10 strength \t30 agility \t10 luck \t25 health \t15 defense
    Fairy -  \t10 strength \t20 agility \t30 luck \t25 health \t15 defense

    Strenght - +1 max dmg
    Agility - +1% dodge
    Luck - +1% critical dmg (2.5 x dmg)

    ''')

    race = input("Enter race:  ")
    while race.lower() != 'human' and race.lower() != 'orc' and \
            race.lower() != 'elf' and race.lower() != 'fairy':
        print('\nPlease choose: Human or Orc or Elf or Fairy')
        race = input("Enter race:  ")

    race_stats = {}
    while race_stats == {}:
        if race == 'human':
            stats = {'strength': 20, 'agility': 15, 'luck': 15,
                     'health': 15, 'defense': 15}
            race_stats.update(stats)

        elif race == 'orc':
            stats = {'strength': 30, 'agility': 10, 'luck': 10,
                     'health': 20, 'defense': 20}
            race_stats.update(stats)

        elif race == 'elf':
            stats = {'strength': 10, 'agility': 30, 'luck': 10,
                     'health': 25, 'defense': 15}
            race_stats.update(stats)

        elif race == 'fairy':
            stats = {'strength': 10, 'agility': 20, 'luck': 30,
                     'health': 20, 'defense': 10}
            race_stats.update(stats)

    print("\nYour character has the following attributes:")
    for attribute, points in race_stats.items():
        print("\t{} :  \t {}".format(attribute.title(), points))

    return race_stats


def player_stats():
    os.system("cls")

    race_stats = choose_race()

    print("""
        You have 40 points in a pool to spend as you wish on the attributes:
            Strength, Agility, Luck, Health, Defense
        If you choose to, you can then take points from an attribute and put them back
        in the pool.

        Strenght - +1 min and max dmg,
        Agility - +1% evade,
        Luck - +1% critical chance dmg (2 x dmg),
        Health - +5 health,
        Defense - -1 dmg reduce

        """
          )

    attributes = copy.deepcopy(race_stats)
    max_pool = 40
    pool = 40

    choice = None
    choice_sentence = """
        \n\nWhat would you like to do?
        0 - Start Game
        1 - Spend points on an attribute
        2 - Put points into pool
        """

    attribute_list = """
        \t - Strength
        \t - Agility
        \t - Luck
        \t - Health
        \t - Defense
        """

    while choice != "0":
        print("\nYour character has the following attributes:")
        for attribute, points in attributes.items():
            print("\t{} :  \t {}".format(attribute.title(), points))
        print("\nThere are {} points in the pool.".format(pool))
        print(choice_sentence)

        choice = input("Choice: ")
        while choice != "0" and choice != "1" and choice != "2":
            print("Invalid choice")
            print(choice_sentence)
            choice = input("Choice: ")
        while choice == "1":  # spend points on an attribute
            if pool == 0:
                print("Sorry, you don't have enough points.")
                break
            print("\nYou have {} points left in pool.".format(pool))
            print("\nWhich attribute would you like to add to?")
            print(attribute_list)

            change_attributes = input("Attribute to change: ")
            while (
                   change_attributes.lower() != "strength" and
                   change_attributes.lower() != "agility" and
                   change_attributes.lower() != "luck" and
                   change_attributes.lower() != "health" and
                   change_attributes.lower() != "defense"
            ):
                print("That is an invalid choice.")
                print("Which attribute would you like to add to?")
                print(attribute_list)
                change_attributes = input("Attribute to change: ")
            else:
                points = int(input("How many points would you like to spend?: "))
                while points > pool:
                    print("That's too many points. You have {} to spend".format(pool))
                    points = int(input("How many points would you like to spend?: "))

            attributes[change_attributes.lower()] += points
            pool -= points
            print("\nYour attributes")
            for attribute, points in attributes.items():
                print("\t{} :  \t {}".format(attribute.title(), points))
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

        while choice == "2":
            if pool == max_pool:  # pool already full
                print("\nSorry, you have no points in your attributes."
                      "\nTry adding some points to your attributes first.")
                break

            print("\nWhich attribute would you like to take points out of?")
            for attribute, points in attributes.items():
                print("\t{} :  \t {}".format(attribute.title(), points))
            change_attributes = input("Choice: ")
            while (
                    change_attributes.lower() != "strength" and
                    change_attributes.lower() != "agility" and
                    change_attributes.lower() != "luck" and
                    change_attributes.lower() != "health" and
                    change_attributes.lower() != "defense"
            ):
                print("\nThat is an invalid choice.")
                print("\nWhich attribute would you like to take points out of?")
                for attribute, points in attributes.items():
                    print("\t{} :  \t {}".format(attribute.title(), points))
                change_attributes = input("Choice: ")

            while attributes[change_attributes.lower()] == 0:
                # when pool of points is zero
                print("You don't have any points in that attribute.")
                change_attributes = input("Choice: ")
                while (
                        change_attributes.lower() != "strength" and
                        change_attributes.lower() != "agility" and
                        change_attributes.lower() != "luck" and
                        change_attributes.lower() != "health" and
                        change_attributes.lower() != "defense"
                ):
                    print("That is an invalid choice.")
                    print("Which attribute would you like to take points out of?")
                    change_attributes = input("Choice: ")
            points = int(input("\nHow many points would you like to remove?: "))

            while points > attributes[change_attributes.lower()]:
                # not enough points in attribute
                print("Sorry, that's too many points! You only have {} "
                      "in {} ".format(attributes[change_attributes.lower()], change_attributes.lower()))
                points = int(input("\nHow many points would you like to remove?: "))

            check_stats = attributes[change_attributes.lower()] - points
            while check_stats < race_stats[change_attributes.lower()]:
                # cant change constant value in race_stats
                print("Sorry, You cant change basic race stats. Your race stat is {} "
                      "in {}. ".format(race_stats[change_attributes.lower()], change_attributes.lower()))
                points = 0
                choice = '2'
                break

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
            print("You now have {} points left in your pool.".format(pool))

    return attributes['strength'], attributes['agility'], attributes['luck'], \
           attributes['health'], attributes['defense']


def choose_class():
    # 1 - Warrior - +10% damage and +10% defence
    # 2 - Rogue - +10% evade and +10% critical chance
    # 3 - Monk - +20% health
    pass