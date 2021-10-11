import random
import sys
import os
import time

player = {}

def main():
    print('Bienvenu !')
    print('1. Start')
    print('2. Load')
    print('3. About')
    print('4. Exit')
    option = int(input())

    if option == 1:
        startnew()

    elif option == 2:
        print('r')

    elif option == 3:
        print('r')

    else:
        sys.exit()

def startnew():


    print('Quel est votre pseudo')
    pseudo = input()

    global player
    player['Name'] = pseudo
    player['Experience'] = 0
    player['Experienceneed'] = 50
    player['Level'] = 1
    player['Attack'] = 30
    player['Health'] = 100
    player['Max_Health'] = 100
    player['Potion'] = 0
    player['WeaponUse'] = None
    start1()
    return player
    
def start1():
    print('\nVous vous reveillez au milieu d\'un endroit mais ou ?')
    print('Essayez de trouver pourquoi vous etes la.')
    print('Bon courage.')
    time.sleep(5)
    print(player_location)
    
def shop():
    print('Bonjour, chère aventurier. Que voulez-vous acheter')
    print('1. Potion')
    print('2. Armes')
    choice = int(input())
    if choice == 1:
        print('Vous avez acheté une petite potion')
        player['Potion'] = player['Potion'] + 1
    if choice == 2:
        print('1. épée en bois')
        print('2. épée en pierre')
        print('3. épée en fer')
        print('4. épée en or')
        print('5. épée enchanté')
        if choice == 1:
            print('Vous avez acheté une épée en bois pour 10')
            player['Attack'] = player['Attack'] + 3
        elif choice == 2:
            print('Vous avez acheté une épée en pierre pour 30')
            player['Attack'] = player['Attack'] + 5
        elif choice == 3:
            print('Vous avez acheté une épée en fer pour 40')
            player['Attack'] = player['Attack'] + 7
        elif choice == 4:
            print('Vous avez acheté une épée en or pour 50')
            player['Attack'] = player['Attack'] + 10
        elif choice == 5:
            print('Vous avez acheté une épée enchanté pour 60 ')
            player['Attack'] = player['Attack'] + 15
    print(player_location)
    return player
    
ennemy = None

def mobchoicefight(): 
    global ennemy
    choice = random.randint(1,2)
    if choice == 1:
        loup={}
        loup['Nom'] = 'Loup'
        loup['Attack'] = 10
        loup['Health'] = 30
        loup['Max.Health'] = 30
        Sanglier['Experiencegive'] = 20
        loup['GoldGain'] = 5
        ennemy = loup
        return ennemy
    elif choice == 2:
        Gobelin = {}
        Gobelin['Nom'] = 'Gobelin'
        Gobelin['Attack'] = 13
        Gobelin['Health'] = 20
        Gobelin['Max.Health'] = 20
        Sanglier['Experiencegive'] = 20
        Gobelin['GoldGain'] = 7
        ennemy = Gobelin
        prefight()
        return ennemy
    elif choice == 3:
        Bandits = {}
        Bandits['Nom'] = 'Bandits'
        Bandits['Attack'] = 17
        Bandits['Health'] = 40
        Bandits['Max.Health'] = 40
        Sanglier['Experiencegive'] = 20
        Bandits['GoldGain'] = 14
        ennemy = Gobelin
        prefight()
        return ennemy
    elif choice == 4:
        Ogre = {}
        Ogre['Nom'] = 'Ogre'
        Ogre['level'] = 1
        Ogre['Attack'] = 15
        Ogre['Health'] = 35
        Ogre['Max.Health'] = 35
        Sanglier['Experiencegive'] = 20
        Ogre['GoldGain'] = 13
        ennemy = Gobelin
        prefight()
        return ennemy
    elif choice == 5:
        Sanglier = {}
        Sanglier['Nom'] = 'Sanglier'
        Sanglier['level'] = 1
        Sanglier['Attack'] = 9
        Sanglier['Health'] = 30
        Sanglier['Max.Health'] = 30
        Sanglier['Experiencegive'] = 20
        Sanglier['GoldGain'] = 9
        ennemy = Gobelin
        prefight()
        return ennemy
    

First = None
def prefight():

    global First
    global ennemy
    First = random.randint(1,4)
    if First >= 4:
        First = 1
        print('Vous commencez en premier')                     
    else:
        First = 2
        print(ennemy , 'commence en premier')
    fight()
    return First

def fight():
    
    global First
    global ennemy
    global player
    
    while player['Health'] != 0 or ennemy['Health'] != 0:
        if First == 1:
            print('Que Voulez-vous faire ')
            print('1. Attaquer')
            print('2. Boire une potion')
            print('3. Fuire')
            choice = int(input())
            if choice == 1:
                print('Vous retirer', player['Attack'])
                ennemy['Health'] - player['Attack']
            if choice == 2:
                if player['Potion'] == 0:
                    print('vous n\'avez pas assez de potion')
                    fight()
                else:
                    print('Vous buvez une potion')
                    player['Health'] = player['Health'] + 30
                    if player['Health'] < 100:
                            player['Health'] = 100
                            fight()

    if player['Health'] == 0:
       print('Vous avez été vaincu')
       mort()
    else:
        print('Vous avez battu', ennemy['Nom'], 'vous remporter', ennemy['Gold'],'.')
        if player['Experience'] <= player['Experienceneed']:
            player['Level'] = player['Level'] + 1
            print('Vous avez gagné un niveau, vous etes maintenant niveau', player['Level'])
        print('Vous avez gagné', ennemy['Experience'],'.' )
        print(player_location)

def prefightboss():
    
    global First
    global boss
    First = random.randint(1,4)
    if First >= 4:
        First = 1
        print('Vous commencez en premier')                     
    else:
        First = 2
        print(boss , 'commence en premier')
    fightboss()
    return First

def fightboss():
    while player['Health'] != 0 or boss['Health'] != 0:
        if First == 1:
            print('Que Voulez-vous faire ')
            print('1. Attaquer')
            print('2. Boire une potion')
            print('3. Fuire')
            choice = int(input())
            if choice == 1:
                print('Vous retirer', player['Attack'])
                boss['Health'] - player['Attack']
            if choice == 2:
                if player['Potion'] == 0:
                    print('vous n\'avez pas assez de potion')
                    fight()
                else:
                    print('Vous buvez une potion')
                    player['Health'] = player['Health'] + 30
                    if player['Health'] < 100:
                            player['Health'] = 100
                            fight()

    if player['Health'] == 0:
       print('Vous avez été vaincu')
       mort()
    else:
        print('Vous avez battu', ennemy['Nom'], 'vous remporter', ennemy['Gold'],'.')
        if player['Experience'] <= player['Experienceneed']:
            player['Level'] = player['Level'] + 1
            print('Vous avez gagné un niveau, vous etes maintenant niveau', player['Level'])
        print('Vous avez gagné', ennemy['Experience'],'.' )
        print(player_location)
def mort():
        print('Vous etes mort')
        print('Voulez-vous recommencer ?')
        print('1. Oui ?')
        print('2. Non')
        choice = int(input())
        print(choice)
        if choice == 1:
            main()
        elif choice == 2:
            sys.exit()
        else:
            print('Veuillez choisir entre 1 ou 2')
            mort()
player_location = None
boss = None

def a1():
    
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Sud')
    print('2. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b1()
        print(player_location)
    elif choice ==2:
        player_location = a2()
        print(player_location)
    else:
        a1()

    return player_location

def a2():
    
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Sud')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b2()
        print(player_location)
    elif choice ==2 :
        player_location = a1()
        print(player_location)
    elif choice ==3 :
        player_location = a3()
        print(player_location)
    else:
        a2()
    return player_location    

def a3():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Sud')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b3()
        print(player_location)
    elif choice ==2 :
        player_location = a2()
        print(player_location)
    elif choice ==3 :
        player_location = a4()
        print(player_location)
    else:
        a3()
    return player_location
    

def a4():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Sud')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b4()
        print(player_location)
    elif choice ==2 :
        player_location = a3()
        print(player_location)
    elif choice ==3 :
        player_location = a5()
        print(player_location)
    else:
        a4()
    return player_location
    
    
    

def a5():
    global player_location
    coffre()
    print('\nOu voulez-vous aller ?')
    print('1. Sud')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b5()
        print(player_location)
    elif choice ==2 :
        player_location = a4()
        print(player_location)
    elif choice ==3 :
        player_location = a6()
        print(player_location)
    else:
        a5()
    return player_location
    

def a6():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Sud')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b6()
        print(player_location)
    elif choice ==2 :
        player_location = a5()
        print(player_location)
    elif choice ==3 :
        player_location = a7()
        print(player_location)
    else:
        a6()
    return player_location
    

def a7():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Sud')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b7()
        print(player_location)
    elif choice ==2 :
        player_location = a6()
        print(player_location)
    elif choice ==3 :
        player_location = a8()
        print(player_location)
    else:
        a7()
    return player_location
    

def a8():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Sud')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b8()
        print(player_location)
    elif choice ==2 :
        player_location = a7()
        print(player_location)
    elif choice ==3 :
        player_location = a8()
        print(player_location)
    else:
        a8()
    return player_location
    

def a9():

    global player_location
    global boss

    print('/!\ Attention /!\ ')
    print('Vous vous trouvez actuellement devant le boss : Frankenstein')
    print('Il ne vous a pas encore vu\nVoulez vous l\'affronter ?')
    print('1. Oui\n2. Non')
    choice = int(input())
    if choice == 1:
        Frankenstein = {}
        Frankenstein['Nom'] = 'Frankenstein'
        Frankenstein['Attack'] = 30
        Frankenstein['Health'] = 70
        Frankenstein['Max.Health'] = 70
        Frankenstein['Experiencegive'] = 40
        Frankenstein['GoldGain'] = 30
        boss = Frankenstein
        fightboss()
        return boss
    elif choice == 2:
        print('\nOu voulez-vous aller ?')
        print('1. Sud')
        print('2. Est')
        choice = int(input())
        if choice == 1:
            player_location = b9()
            print(player_location)
        elif choice ==2 :
            player_location = a8()
            print(player_location)
        else:
            a9()
    else:
        a9()
    return player_location

def b1():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = a1()
        print(player_location)
    elif choice ==2 :
        player_location = c1()
        print(player_location)
    elif choice ==3 :
        player_location = b2()
        print(player_location)
    else:
        b1()
    return player_location
    

def b2():
    global player_location
    coffre()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = a2()
        print(player_location)
    elif choice ==2 :
        player_location = c2()
        print(player_location)
    elif choice ==3 :
        player_location = b3()
        print(player_location)
    elif choice ==4 :
        player_location = b1()
        print(player_location)
    else:
        b2()
    return player_location
    

def b3():
    global player_location
    shop()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = a3()
        print(player_location)
    elif choice ==2 :
        player_location = c3()
        print(player_location)
    elif choice ==3 :
        player_location = b2()
        print(player_location)
    elif choice ==4 :
        player_location = b4()
        print(player_location)
    else:
        b3()
    return player_location
    

def b4():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = a4()
        print(player_location)
    elif choice ==2 :
        player_location = c4()
        print(player_location)
    elif choice ==3 :
        player_location = b3()
        print(player_location)
    elif choice ==4 :
        player_location = b5()
        print(player_location)
    else:
        b4()
    return player_location
    

def b5(): #Start
    global player_location
    
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = a5()
        print(player_location)
    elif choice ==2 :
        player_location = c5()
        print(player_location)
    elif choice ==3 :
        player_location = b4()
        print(player_location)
    elif choice ==4 :
        player_location = b6()
        print(player_location)
    else:
        b5()
    return player_location
    

def b6():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = a6()
        print(player_location)
    elif choice ==2 :
        player_location = c6()
        print(player_location)
    elif choice ==3 :
        player_location = b5()
        print(player_location)
    elif choice ==4 :
        player_location = b7()
        print(player_location)
    else:
        b6()
    return player_location
    

def b7():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = a7()
        print(player_location)
    elif choice ==2 :
        player_location = c7()
        print(player_location)
    elif choice ==3 :
        player_location = b6()
        print(player_location)
    elif choice ==4 :
        player_location = b8()
        print(player_location)
    else:
        b7()
    return player_location
    

def b8():
    global player_location
    coffre()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = a8()
        print(player_location)
    elif choice ==2 :
        player_location = c8()
        print(player_location)
    elif choice ==3 :
        player_location = b7()
        print(player_location)
    elif choice ==4 :
        player_location = b9()
        print(player_location)
    else:
        b8()
    return player_location
    

def b9():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    choice = int(input())
    if choice == 1:
        player_location = a9()
        print(player_location)
    elif choice ==2 :
        player_location = c9()
        print(player_location)
    elif choice ==3 :
        player_location = b8()
        print(player_location)
    else:
        b9()
    return player_location
    
    

def c1():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b1()
        print(player_location)
    elif choice ==2 :
        player_location = d1()
        print(player_location)
    elif choice ==3 :
        player_location = c2()
        print(player_location)
    else:
        c1()
    return player_location
    

def c2():
    global player_location
    boss2()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b2()
        print(player_location)
    elif choice ==2 :
        player_location = d2()
        print(player_location)
    elif choice ==3 :
        player_location = c1()
        print(player_location)
    elif choice ==4 :
        player_location = c3()
        print(player_location)
    else:
        c2()
    return player_location
    
    

def c3():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b3()
        print(player_location)
    elif choice ==2 :
        player_location = d3()
        print(player_location)
    elif choice ==3 :
        player_location = c2()
        print(player_location)
    elif choice ==4 :
        player_location = c4()
        print(player_location)
    else:
        c3()
    return player_location
    

def c4():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b4()
        print(player_location)
    elif choice ==2 :
        player_location = d4()
        print(player_location)
    elif choice ==3 :
        player_location = c3()
        print(player_location)
    elif choice ==4 :
        player_location = c5()
        print(player_location)
    else:
        c4()
    return player_location
    

def c5():
    global player_location
    coffre()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b5()
        print(player_location)
    elif choice ==2 :
        player_location = d5()
        print(player_location)
    elif choice ==3 :
        player_location = c4()
        print(player_location)
    elif choice ==4 :
        player_location = c6()
        print(player_location)
    else:
        c5()
    return player_location
    

def c6():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b6()
        print(player_location)
    elif choice ==2 :
        player_location = d6()
        print(player_location)
    elif choice ==3 :
        player_location = c5()
        print(player_location)
    elif choice ==4 :
        player_location = c7()
        print(player_location)
    else:
        c6()
    return player_location
    

def c7():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b7()
        print(player_location)
    elif choice ==2 :
        player_location = d7()
        print(player_location)
    elif choice ==3 :
        player_location = c6()
        print(player_location)
    elif choice ==4 :
        player_location = c8()
        print(player_location)
    else:
        c7()
    return player_location
    

def c8():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = b8()
        print(player_location)
    elif choice ==2 :
        player_location = d8()
        print(player_location)
    elif choice ==3 :
        player_location = c7()
        print(player_location)
    elif choice ==4 :
        player_location = c9()
        print(player_location)
    else:
        c8()
    return player_location
    

def c9():
    global player_location
    shop()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    choice = int(input())
    if choice == 1:
        player_location = b9()
        print(player_location)
    elif choice ==2 :
        player_location = d9()
        print(player_location)
    elif choice ==3 :
        player_location = c8()
        print(player_location)
    else:
        c9()
    return player_location
    

def d1():
    global player_location
    shop()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = c1()
        print(player_location)
    elif choice ==2 :
        player_location = e1()
        print(player_location)
    elif choice ==3 :
        player_location = d2()
        print(player_location)
    else:
        d1()
    return player_location
    

def d2():
    global player_location
    coffre()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = c2()
        print(player_location)
    elif choice ==2 :
        player_location = e2()
        print(player_location)
    elif choice ==3 :
        player_location = d1()
        print(player_location)
    elif choice ==4 :
        player_location = d3()
        print(player_location)
    else:
        d2()
    return player_location
    

def d3():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = c3()
        print(player_location)
    elif choice ==2 :
        player_location = e3()
        print(player_location)
    elif choice ==3 :
        player_location = d2()
        print(player_location)
    elif choice ==4 :
        player_location = d4()
        print(player_location)
    else:
        d3()
    return player_location
    

def d4():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = c4()
        print(player_location)
    elif choice ==2 :
        player_location = e4()
        print(player_location)
    elif choice ==3 :
        player_location = d3()
        print(player_location)
    elif choice ==4 :
        player_location = d5()
        print(player_location)
    else:
        d4()
    return player_location
    

def d5():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = c5()
        print(player_location)
    elif choice ==2 :
        player_location = e5()
        print(player_location)
    elif choice ==3 :
        player_location = d4()
        print(player_location)
    elif choice ==4 :
        player_location = d6()
        print(player_location)
    else:
        d5()
    return player_location
    

def d6():
    global player_location
    coffre()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = c6()
        print(player_location)
    elif choice ==2 :
        player_location = e6()
        print(player_location)
    elif choice ==3 :
        player_location = d5()
        print(player_location)
    elif choice ==4 :
        player_location = d7()
        print(player_location)
    else:
        d6()
    return player_location
    

def d7():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = c7()
        print(player_location)
    elif choice ==2 :
        player_location = e7()
        print(player_location)
    elif choice ==3 :
        player_location = d6()
        print(player_location)
    elif choice ==4 :
        player_location = d8()
        print(player_location)
    else:
        d7()
    return player_location
    

def d8():
    global player_location
    coffre()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    print('4. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = c8()
        print(player_location)
    elif choice ==2 :
        player_location = e8()
        print(player_location)
    elif choice ==3 :
        player_location = d7()
        print(player_location)
    elif choice ==4 :
        player_location = d9()
        print(player_location)
    else:
        d8()
    return player_location 
    

def d9():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Sud')
    print('3. Est')
    choice = int(input())
    if choice == 1:
        player_location = c9()
        print(player_location)
    elif choice ==2 :
        player_location = e9()
        print(player_location)
    elif choice ==3 :
        player_location = d8()
        print(player_location)
    else:
        d9()
    return player_location
    

def e1():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = d1()
        print(player_location)
    elif choice ==2 :
        player_location = e2()
        print(player_location)
    else:
        e1()
    return player_location
    

def e2():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = d2()
        print(player_location)
    elif choice ==2 :
        player_location = e1()
        print(player_location)
    elif choice ==3 :
        player_location = e3()
        print(player_location)
    else:
        e2()
    return player_location
    

def e3():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = d3()
        print(player_location)
    elif choice ==2 :
        player_location = e2()
        print(player_location)
    elif choice ==3 :
        player_location = e4()
        print(player_location)
    else:
        e3()
    return player_location
    

def e4():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = d4()
        print(player_location)
    elif choice ==2 :
        player_location = e3()
        print(player_location)
    elif choice ==3 :
        player_location = e5()
        print(player_location)
    else:
        e4()
    return player_location

def e5():
    global player_location
    shop()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = d5()
        print(player_location)
    elif choice ==2 :
        player_location = e4()
        print(player_location)
    elif choice ==3 :
        player_location = e6()
        print(player_location)
    else:
        e5()
    return player_location
    

def e6():
    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = d6()
        print(player_location)
    elif choice ==2 :
        player_location = e5()
        print(player_location)
    elif choice ==3 :
        player_location = e7()
        print(player_location)
    else:
        e6()
    return player_location



def boss2():

    print('/!\ Attention /!\ ')

def boss3():

    print('/!\ Attention /!\ ')

def e7():
    global player_location
    boss3()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = d7()
        print(player_location)
    elif choice ==2 :
        player_location = e6()
        print(player_location)
    elif choice ==3 :
        player_location = e8()
        print(player_location)
    else:
        e7()
    return player_location
    

def e8():
    global player_location

    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Est')
    print('3. Ouest')
    choice = int(input())
    if choice == 1:
        player_location = d8()
        print(player_location)
    elif choice ==2 :
        player_location = e7()
        print(player_location)
    elif choice ==3 :
        player_location = e9()
        print(player_location)
    else:
        e8()
    return player_location
    

def e9():

    global player_location
    nothing()
    print('\nOu voulez-vous aller ?')
    print('1. Nord')
    print('2. Est')
    choice = int(input())
    if choice == 1:
        player_location = d9()
        print(player_location)
    elif choice ==2 :
        player_location = e8()
        print(player_location)
    else:
        e9()
    return player_location

def nothing():
    chancefight = random.randint(1,4)
    if chancefight < 2:
        mobchoicefight()
    else:
        print(player_location)

def coffre():
    print('\nIl y a un coffre voulez-vous l\'ouvrir ?')
    print('1. Oui')
    print('2. Non')


main()
player_location = b5()