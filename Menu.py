
import sys
from Battle import *
from AboutMe import *
from Scores import *

#Intro
def display_intro1():
    print('''
--+--------------------------------------------------------------------+-- 
  |                                                                    |    
  |   __                 _      _                                      |    
  |  / _|  _        _   | \    / |  _   _       _                      |    
  | | |_  |_| |  | |_   |  \/\/  | | | |_| ||  | \                     |    
  |  \__| | |  \/  |_   |___/\___| |_| | \ ||_ |_/                     |    
  |                                                                    |    
  | ==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--== |    
  |      Hello Adventurer!               Welcome to CaveWorld!         |
  |                                                                    |    
--+--------------------------------------------------------------------+--
  '                                                                    '     ''')
    time.sleep(2)
    os.system("cls")

def display_intro2():
        print('''

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
        time.sleep(2)
        os.system("cls")




# Main menu

def main_menu():
    display_intro1()
    display_intro2()
    choice = None

    while choice != '4':

        print(
                """
        --------------------
        |       Menu       |
        --------------------
        |   1 - New Game   |
        --------------------
        |   2 - Scores     |
        --------------------
        |   3 - About Me   |
        --------------------
        |   4 - Exit       |
        --------------------

            """)
        choice = input("Choice: ")
        print()

        # NewGame
        if choice == "1":

            player = create_character()
            battle(player)
            return main_menu()

        # Scores
        elif choice == "2":
            scores_load()

        # About Me
        elif choice == "3":
            about_me()
            key = input('\t\t\t====press KEY to return====')
            if key != "":
                return main_menu()

        # Exit
        elif choice == "4":
            print("Goodbye!")
            sys.exit()

        # Unknown choice
        else:
            print(f"Sorry, but {choice} isn't a valid choice.")


if __name__ == "__main__":
    main_menu()