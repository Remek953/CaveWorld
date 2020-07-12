
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
    Human -  \t2 str \t2 agility \t1 luck
    Orc -  \t3 str \t1 agility \t1 luck
    Elf - \t1 str \t3 agility \t1 luck
    Fairy - \t1 str \t1 agility \t3 luck
    ''')
    race = input("Enter race:  ")
    while race.lower() != 'human' and race.lower() != 'orc' and race.lower() != 'elf' and race.lower() != 'fairy':
        print('\nPlease choose: Human or Orc or Elf or Fairy')
        race = input("Enter race:  ")




