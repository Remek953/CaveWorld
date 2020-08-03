import random,time

def battle_intro():

    b_intro = random.randint(1,3)

    if b_intro == 1:
        print('''
    
        The world is in chaos and now there is no one to stop you from gain glory and fame.
        Use your magnificent and innate skills to kill as many monsters as possible.
        Good Luck!
        
        
        ''')
    elif b_intro == 2:
        print('''
        15 years ago, the first “portal” that connected the real world with the monster world opened.
        People received the power to hunt monsters within the portal. They are known as "Hunters".
        You enter the first "A" level portal to find legendary sword.  
        
        
        ''')


    elif b_intro == 3:
        print('''
        You was wrongly accused of murder. You have been sent to The CaveWorld - the most dangerous prison on the world. 
        You will spend the rest of your life in tha place. 
        Escape from prison and prove your innocent.
        
        ''')

def 1():
    orcs_count = 0

    while hero_health > 0:
      # hero_damage = random.randint(1, 10 + add_str )
        orc_damage = random.randint(1, 10)
        orcs_count += 1
        hero_health -= orc_damage

        print('Your hero defeated orcs but takes {} damage. Your total health is: {}'.format(orc_damage, hero_health))
        time.sleep(1)

    print("Your hero died but defeated {} orcs.".format(orcs_count)) #hero_name

play()
