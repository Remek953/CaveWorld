import random



class Monster():
    """
    Class represents the enemy stats.
    """


    def __init__(self, name, base_attack, defense, max_health,
                 evade_chance, critical_chance, hit_chance, evade, points):
        self.name = name
        self.base_attack = base_attack
        self.defense = defense
        self.max_health = max_health
        self.health = self.max_health
        self.evade_chance = evade_chance
        self.critical_chance = critical_chance
        self.hit_chance = hit_chance
        self.evade = evade
        self.points = points




    def get_attack(self):
        attack = round(random.uniform(self.base_attack/2, self.base_attack))
        return attack

    def get_hit_chance(self):
        return self.hit_chance

    def get_evade_chance(self):
        return self.evade

    def get_critical_chance(self):
        critical = round(random.uniform(0, 10), 2)
        return critical

    def get_critical_dmg(self):
        critical_dmg = 2 * self.get_attack()
        return critical_dmg

    def is_dead(self):
        if self.health <= 0:
            print(f"{self.name.title()} has been slayed.")
            return True
        else:
            return False
"""
    def count_kill(self):
        if self.is_dead() is True:
            point += self.points
            print("test!!!!!!!!!!!!!")
            return point
        else:
            return False

"""



class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", 10, 5, 150, 5, 5, 15, 6, 5)

    def display(self):
        print(" A dangerous orc has appeared!")
        print("""
                            (    )
                          ((((()))
                          |o\ /o)|
                          ( (  _')
                           (._.  /\__
                           """)


class Bat(Monster):
    def __init__(self):
        super().__init__("Bat", 20, 5, 150, 5, 5, 10, 6, 0)

    def display(self):
        print(" A wicked bat has appeared!")
        print("""

                =/\                 /\=
                / \\'._   (\_/)   _.'/ \\
               / .''._'--(o.o)--'_.''. \\
              /.' _/ |`'=/ " \='`| \_ `.\\
             /` .' `\;-,'\___/',-;/` '. '\\
            /.-' jgs   `\(-V-)/`       `-.\\
            `            "   "            `


        ------------------------------------------------
        This ASCII pic can be found at
        https://asciiart.website/index.php?art=animals/bats

            """)


class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", 15, 20, 100, 5, 5, 15, 0)


    def display(self):
        print(" A murderous skeleton has appeared!")
        print("""
            
                        ,--.
                       ([ oo]
                        `- ^\\
                      _  I`-'
                    ,o(`-V'
                    |( `-H-'
                    |(`--A-'
                    |(`-/_\\'\\
                    O `'I ``\\\\
                    (\  I    |\,
                     \\\\-T-"`, |H   Ojo
            
            ------------------------------------------------
            This ASCII pic can be found at
            https://asciiart.website/index.php?art=people/skeletons
            
                """)



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
     \   \\\\     ( '        )(    )
      \   \\\\    \.  _.__ ____( .  |
       \  /\\\\   .(   .'  /\  '.  )
        \(  \\\\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\\\ .( |\/\/\/\/\/|
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





