
def hero_name():
    print('Choose your name. Min 1 and max 12 characters')
    username = input("Enter name:  ")
    while True:
        if (len(username) < 1):
                    print('Choose your name. Min 1 and max 12 characters')
                    print("Username too short")
                    username = input("Enter name:  ")
        elif (len(username) > 12):
                    print('Choose your name. Min 1 and max 12 characters')
                    print("Username too long")
                    username = input("Enter name:  ")


def hero_race():

    print('''Choose your race: 
    Human -  \t2 strength \t2 agility \t1 luck
    Orc -    \t3 strength \t1 agility \t1 luck
    Elf -    \t1 strength \t3 agility \t1 luck
    Fairy -  \t1 strength \t1 agility \t3 luck
    
    Strenght - +1 max dmg
    Agility - +1% dodge
    Luck - +1% critical dmg (2.5 x dmg)
    
    ''')
    race = input("Enter race:  ")
    while race.lower() != 'human' and race.lower() != 'orc' and race.lower() != 'elf' and race.lower() != 'fairy':
        print('\nPlease choose: Human or Orc or Elf or Fairy')
        race = input("Enter race:  ")

    race_stats = {}

    if race == 'human':
         stats = {'strength': 2, 'agility': 1, 'luck': 1}
         race_stats.update(stats)

    elif race == 'orc':
         stats = {'strength': 3, 'agility': 1, 'luck': 1}
         race_stats.update(stats)

    elif race == 'elf':
         stats = {'strength': 1, 'agility': 3, 'luck': 1}
         race_stats.update(stats)

    elif race == 'fairy':
         stats = {'strength': 1, 'agility': 1, 'luck': 3}
         race_stats.update(stats)

    print("\nYour character has the following attributes:")
    for attribute, points in race_stats.items():
        print("\t{} :  \t {}".format(attribute.title(), points))








def hero_stats():

    print("""
    You have 20 points in a pool to spend as you wish on the attributes:
        Strength, Agility, Luck
    If you choose to, you can then take points from an attribute and put them back
    in the pool.
    
    Strenght - +1 max dmg
    Agility - +1% dodge
    Luck - +1% critical dmg (2 x dmg)
    
    """
          )

    attributes =  {'strength': 3, 'agility': 1, 'luck': 1} #change to race_stats
    pool = 20

    choice = None
    choice_sentence = """
    \n\nWhat would you like to do?
    0 - Next
    1 - Spend points on an attribute
    2 - Put points into pool
    """

    attribute_list = """
    \t - Strength
    \t - Agility
    \t - Luck
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
            while (change_attributes.lower() != "strength" and
                   change_attributes.lower() != "agility" and
                   change_attributes.lower() != "luck"):
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

        while choice == "2":  # add points to pool
            if pool == 20:  # pool already full
                print("\nSorry, you have no points in your attributes."
                      "\nTry adding some points to your attributes first.")
                break

            print("\nWhich attribute would you like to take points out of?")
            for attribute, points in attributes.items():
                print("\t{} :  \t {}".format(attribute.title(), points))
            change_attributes = input("Choice: ")
            while (change_attributes.lower() != "strength" and
                   change_attributes.lower() != "agility" and
                   change_attributes.lower() != "luck"):
                print("\nThat is an invalid choice.")
                print("\nWhich attribute would you like to take points out of?")
                for attribute, points in attributes.items():
                    print("\t{} :  \t {}".format(attribute.title(), points))
                change_attributes = input("Choice: ")

            while attributes[change_attributes.lower()] == 0:
                # no points can be removed, change this to race stats!
                print("You don't have any points in that attribute.")
                change_attributes = input("Choice: ")
                while (change_attributes.lower() != "strength" and
                       change_attributes.lower() != "agility" and
                       change_attributes.lower() != "luck"):
                    print("That is an invalid choice.")
                    print("Which attribute would you like to take points out of?")
                    change_attributes = input("Choice: ")
            points = int(input("\nHow many points would you like to remove?: "))
            while points > attributes[change_attributes.lower()]:
                # not enough points in attribute
                print("Sorry, that's too many points! You only have {} "
                      "in {} ".format(attributes[change_attributese], change_attributes))
                points = int(input("\nHow many points would you like to remove?: "))
            print("OK!")
            pool += points
            attributes[change_attributes.lower()] -= points
            print("You now have {} points left in your pool.".format(pool))

            another_change = input("\nWant to change another attribute? Yes or No: ")
            while another_change.lower() != "yes" and another_change.lower() != "no" \
                and another_change.lower() != "y" and another_change.lower() != "n":
                print("That's an invalid choice.")
                another_change = input("Want to change another attribute? Yes or No: ")
            if another_change.lower() == "no" or another_change.lower() == "n":
                break






