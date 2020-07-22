class Orc(object):
    def __init__(self):
        self.name = "Orc"
        self.max_health = 150
        self.health = self.max_health
        self.attack = 25
        self.defense = 20
        self.evade_chance = 2
        self.crit_chance = 5

class Bat(object):
    def __init__(self):
        self.name = "Goblin"
        self.max_health = 50
        self.health = self.max_health
        self.attack = 10
        self.defense = 5
        self.evade_chance = 2
        self.crit_chance = 5

class Skeleton(object):
    def __init__(self):
        self.name = "Skeleton"
        self.max_health = 100
        self.health = self.max_health
        self.attack = 15
        self.defense = 10
        self.evade_chance = 2
        self.crit_chance = 5


def display_orc():
    print("""
                    (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"

------------------------------------------------
Thank you for visiting https://asciiart.website/
This ASCII pic can be found at
https://asciiart.website/index.php?art=creatures/monsters

    """)


def display_goblin():
    print("""
        =/\                 /\=
        / \'._   (\_/)   _.'/ \
       / .''._'--(o.o)--'_.''. \
      /.' _/ |`'=/ " \='`| \_ `.\
     /` .' `\;-,'\___/',-;/` '. '\
    /.-' jgs   `\(-V-)/`       `-.\
    `            "   "            `

------------------------------------------------
Thank you for visiting https://asciiart.website/
This ASCII pic can be found at
https://asciiart.website/index.php?art=animals/bats

    """)


def display_Skeleton():
    print("""
            ,--.
           ([ oo]
            `- ^\
          _  I`-'
        ,o(`-V'
        |( `-H-'
        |(`--A-'
        |(`-/_\'\
        O `'I ``\\
        (\  I    |\,
         \\-T-"`, |H   Ojo

------------------------------------------------
Thank you for visiting https://asciiart.website/
This ASCII pic can be found at
https://asciiart.website/index.php?art=people/skeletons

    """)



