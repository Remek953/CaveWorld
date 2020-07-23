import random,time









def play():
    print('''

    The world is in chaos and now there is no one to stop you from gain glory and fame.
    Use your magnificent and innate skills to kill as many monsters as possible.
    Good Luck!
    
    
    ''')


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
