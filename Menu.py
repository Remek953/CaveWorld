import time
import sys, os
from Battle import *

#Intro
def display_intro():
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
          
          
                 .......::::::::::::)..           .......................(::::::........
          .:::::;;;;;;;;):::::::.... .           .......:::::::::::::<......
              <  >>>                   ,.
      .::..  ;   I;L\  /L\.  ..::..   /iL.           |         ..::::::::::::..
            ;    II;L\/LLLL;         / I;L\    \     |     / /\_   Collage by
                 II;..LLLLLL\    _._/ I;:.L\     \   |   / _/J; \    Bob Allison
          :     IIIIi;..LLLLL\__/   IIII:..L\____  \###/  /JJI:  \\
        ,;     ILIi;;;:...:LLL;\      IIIII;.LLLLL\#####/JJ II;   \\
       ;     I LLii;;;.:.. :LLL;\     III;;;::LLLLL\###/JJ IIII;   \_.
      :     IIILiii;;::.... :LLL;|      ;;I;;::.:LLLLLL:;IJ IIIII;:   \__.
               IIIII IIii;;::;..;\          ;;:::...LLLL;IJIII;;    :::   \\
    :    ;    IIIIIIIIIii;;::.;..      _==|      ;..  :;IJIII;:::    ::    \\
        ;    ::::::::::::;;::..;  _==|   )__)  |                            \\
     '  '"  "  ""'""'""  ""'"  '"    )_)  )___) ))  ""''"   ""'"  "'" "'"'"'  "'""
            '""   ""^^       ^~   )___) )____))_)   ~~         ""^^^""  '  "  "~"
    ' ^^            ^        _    )____)_____))__)\      ~^~~^           ^^"
         '^^          ^~      \---__|____/|___|___-\\--        "~"~         "~"
       ''    '^          ~"~   \   oo oo oo oo     /      ~"      '~       ""~"
            ____   ^^^"~   ~~^^^^^^^^^^^^^^^^^^^^^^    ^~^            ^~^^^
          /  o   \     ""'"  __          __ "'"''     '   ''~     ~""~"`    ""''
        < ____     \\"'"    /    \   "' /    \       _          _    "~    _
              |     |     |  __  |    |  __  |    /   \      /   \       / |
        '     |_____|  '  |__||__|    |__||__| ' |_____| '' |_____| ""  /_/
            ""  ~^^^^      '"""^^'''''        '''''''""        '''''^^""
       ''          '^^           ~^^~          ~^ '      ~~      '  ^   ^^^^^^^^

            ------------------------------------------------
            This ASCII pic can be found at
            https://asciiart.website/index.php?art=creatures/monsters
               
          
          ''')
    #time.sleep(1)
    #os.system("cls")




# Main menu

def main_menu():
    #display_intro()
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

            player = player23()
            battle(player)

            return main_menu()

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
            sys.exit()

        # Unknown choice
        else:
            print(f"Sorry, but {choice} isn't a valid choice.")

        points.result()


#########################

main_menu()