import random



class Monster():
    """
    Class represents the enemy stats.
    """
    def __init__(self, name, base_attack, defense, max_health,
                  critical_chance, hit_chance, evade, points):
        self.name = name
        self.base_attack = base_attack
        self.defense = defense
        self.max_health = max_health
        self.health = self.max_health
        self.critical_chance = critical_chance
        self.hit_chance = hit_chance
        self.evade = evade
        self.points = points

    def get_attack(self):
        attack = round(random.uniform(self.base_attack/3, self.base_attack))
        return attack

    def get_defense(self):
        return self.defense

    def get_hit_chance(self):
        return self.hit_chance

    def get_evade_chance(self):
        evade = self.evade
        return evade

    def get_critical_chance(self):
        critical = round(random.uniform(0, 10), 2)
        return critical

    def get_critical_dmg(self):
        critical_dmg = round(2 * self.get_attack(), 1)
        return critical_dmg

    def is_dead(self):
        if self.health <= 0:
            print(f"{self.name.title()} has been slayed.")
            return True
        else:
            return False

    def count_kill(self):
            return self.points


class Orc(Monster):
    def __init__(self):
        super().__init__("orc", 40, 25, 200, 6, 8, 3, 10)

    def display(self):
        print(f" A dangerous {self.name} has appeared!")
        print("""
                            (    )
                          ((((()))
                          |o\ /o)|
                          ( (  _')
                           (._.  /\__
                           """)


class Bat(Monster):
    def __init__(self):
        super().__init__("bat", 10, 5, 100, 4, 7, 5, 2)

    def display(self):
        print(f" A wicked {self.name} has appeared!")
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
        super().__init__("skeleton", 25, 10, 200, 5, 7, 2, 5)


    def display(self):
        print(f" A murderous {self.name} has appeared!")
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


class Ant(Monster):
    def __init__(self):
        super().__init__("giant ant", 30, 25, 350, 4, 7, 4, 6)

    def display(self):
        print(f" A {self.name} has appeared!")
        print("""
        
             \       /
              \     /  
               \.-./ 
              (o\^/o)  _   _   _     __
               ./ \.\ ( )-( )-( ) .-'  '-.
                {-} \(//  ||   \\\\/ (   )) '-.
                     //-__||__.-\\\\.       .-'
                    (/    ()     \)'-._.-'
                    ||    ||      \\\\
            MJP     ('    ('       ')
            
            ------------------------------------------------
            Thank you for visiting https://asciiart.website/
            This ASCII pic can be found at
            https://asciiart.website/index.php?art=animals/insects/ants


                """)


class Scorpion(Monster):
    def __init__(self):
        super().__init__("deadly scorpion", 60, 5, 75, 7, 7, 6, 8)

    def display(self):
        print(f" A {self.name} has appeared!")
        print("""
        
               ___ __ 
             _{___{__}\\
            {_}      `\)            
           {_}        `            _.-''''--.._
           {_}                    //'.--.  \___`.
            { }__,_.--~~~-~~~-~~-::.---. `-.\  `.)
             `-.{_{_{_{_{_{_{_{_//  -- 8;=- `
                `-:,_.:,_:,_:,.`\\\\._ ..'=- , 
                    // // // //`-.`\`   .-'/
             jgs   << << << <<    \ `--'  /----)
                    ^  ^  ^  ^     `-.....--'''
        
        ------------------------------------------------
        Thank you for visiting https://asciiart.website/
        This ASCII pic can be found at
        https://asciiart.website/index.php?art=animals/scorpions
        
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





