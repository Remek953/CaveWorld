#  My first project: CaveWorld. It is a simple game with RPG elements and ASCII graphic.

import time

#Intro
def intro():
    print('''
    - --+--------------------------------------------------------------------+-- -  
        |                                                                    |    
        |   __                 _      _                                      |    
        |  / _|  _        _   | \    / |  _   _       _                      |    
        | | |_  |_| |  | |_   |  \/\/  | | | |_| ||  | \                     |    
        |  \__| | |  \/  |_   |___/\___| |_| | \ ||_ |_/                     |    
        |                                                                    |    
        | ==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--== |    
        |      Hello Adventurer!               Welcome to CaveWorld!         |
        |                                                                    |    
    - --+--------------------------------------------------------------------+-- -
        '                                                                    '     
          ''')
    time.sleep(1)



# Main menu

def main_menu():

    choice = None

    while choice != '4':

        print(
                """
        \tMenu
        \t0 - New Game
        \t1 - Options
        \t2 - Scores
        \t3 - About Me
        \t4 - Exit
            """)
        choice = input("Choice: ")
        print()

        # NewGame
        if choice == "0":
            pass

        # Options
        elif choice == "1":
            pass

        # Scores
        elif choice == "2":
            pass

        # About Me
        elif choice == "3":
            pass

        # Exit
        elif choice == "4":
            print("Goodbye!")
            break

        # Unknown choice
        else:
            print("Sorry, but {} isn't a valid choice.".format(choice))

intro()
main_menu()

#########################

'''TEST'''

