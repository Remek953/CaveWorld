import random


class Monster:
    def __init__(self, name, base_attack, defense, max_health,
                 evade_chance, critical_chance, points, hit_chance):
        self.name = name
        self.base_attack = base_attack
        self.defense = defense
        self.max_health = max_health
        self.health = self.max_health
        self.evade_chance = evade_chance
        self.critical_chance = critical_chance
        self.points = points
        self.hit_chance = hit_chance

    def get_attack(self):
        attack = round(random.uniform(self.base_attack/2, self.base_attack))
        return attack

    def get_critical_dmg(self):
        critical_dmg = 2 * self.get_attack()
        return critical_dmg


orc = Monster("Orc", 25, 20, 150, 5, 5, 25, 8)
bat = Monster("Bat", 10, 5, 150, 5, 5, 10, 6)
skeleton = Monster("Skeleton", 15, 20, 100, 5, 5, 15, 7)



def display_orc():
    print(" A dangerous orc has appeared!")
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
This ASCII pic can be found at
https://asciiart.website/index.php?art=creatures/monsters

    """)


def display_bat():
    print(" A wicked bat has appeared!")
    print("""
    
        =/\                 /\=
        / \'._   (\_/)   _.'/ \
       / .''._'--(o.o)--'_.''. \
      /.' _/ |`'=/ " \='`| \_ `.\
     /` .' `\;-,'\___/',-;/` '. '\
    /.-' jgs   `\(-V-)/`       `-.\
    `            "   "            `


------------------------------------------------
This ASCII pic can be found at
https://asciiart.website/index.php?art=animals/bats

    """)


def display_skeleton():
    print(" A murderous skeleton has appeared!")
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
This ASCII pic can be found at
https://asciiart.website/index.php?art=people/skeletons

    """)



