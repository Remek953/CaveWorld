import random
import time


class Monster:

    """
    Class represents the enemy stats.
    """

    def __init__(self, name, base_attack, defense, max_health, critical_chance, hit_chance, evade, points):

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

        attack = round(random.uniform(self.base_attack/3, self.base_attack), 2)
        return attack

    def get_defense(self):

        return self.defense

    def get_hit_chance(self):

        hit = round(random.uniform(1, self.hit_chance), 2)
        return hit

    def get_evade_chance(self):

        evade = round(random.uniform(1, self.evade), 2)
        return evade

    def get_critical_chance(self):

        critical = round(random.uniform(0, self.critical_chance), 2)
        return critical

    def get_critical_dmg(self):

        critical_dmg = round(2 * self.get_attack(), 2)
        return critical_dmg

    def is_dead(self):

        if self.health <= 0:
            print(f"{self.name.title()} has been slayed.")
            return True

        else:
            return False


class Orc(Monster):

    def __init__(self):
        super().__init__("orc", 50, 25, 250, 6, 9, 3, 10)

    def display(self):
        print(f"\nA dangerous {self.name} has appeared!")
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
        time.sleep(0.8)


class Bat(Monster):

    def __init__(self):
        super().__init__("bat", 20, 5, 100, 4, 9, 5, 2)

    def display(self):
        print(f"\nA wicked {self.name} has appeared!")
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
        time.sleep(0.8)


class Skeleton(Monster):

    def __init__(self):
        super().__init__("skeleton", 35, 10, 200, 5, 9, 2, 5)

    def display(self):
        print(f"\nA murderous {self.name} has appeared!")
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
        time.sleep(0.8)


class Ant(Monster):

    def __init__(self):
        super().__init__("giant ant", 40, 25, 350, 4, 9, 4, 8)

    def display(self):
        print(f"\nA {self.name} has appeared!")
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
        time.sleep(0.8)


class Scorpion(Monster):

    def __init__(self):
        super().__init__("deadly scorpion", 70, 5, 100, 7, 9, 8, 6)

    def display(self):
        print(f"\nA {self.name} has appeared!")
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
        time.sleep(0.8)





