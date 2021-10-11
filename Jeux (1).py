
import random
import sys
import os
import time

player = {}

loup = {}
loup['Combat'] = 0

bandits = {}
bandits['Combat'] = 0

ogre = {}
ogre['Combat'] = 0

sanglier = {}
sanglier['Combat'] = 0

ennemy = None
Nombre_De_Combat = 0
village = None

def main(): 

    # Acceuil

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
        print('Bienvenu dans notre RPG\nLe but est de trouver pourquoi une énergie malfaisante dans les villages aux quatres coin cardinaux')
        print('Vous devez découvrir les mystères que l\'endroit cache')
        time.sleep(3)
        main()

    else:
        sys.exit()

def startnew():

    # description du personnage

    print('Quel est votre pseudo')
    pseudo = input()

    global player
    player['Nom'] = pseudo
    player['Experience'] = 0
    player['Experienceneed'] = 10
    player['Level'] = 1
    player['Attack'] = 30
    player['Defaultatk'] = 30
    player['Health'] = 100
    player['Max_Health'] = 100
    player['Potion'] = 0
    player['Gold'] = 0
    start1()
    return player
    
def start1():

    #Histoire

    print('\nVous avez été appelé car une énergie mysterieuse est présent')
    print('Essayez de trouver la source.')
    print('Bon courage jeune aventurier.')
    time.sleep(5)
    b5()
    
def b5(): #Start choisir le lieux

    global player
    global village
    global loup
    global sanglier
    global ogre
    global bandits

    global Nombre_De_Combat
    if Nombre_De_Combat != 4 :
        print('\nOu voulez-vous aller ?')
        print('1. Nord')
        print('2. Sud')
        print('3. Est')
        print('4. Ouest')
        print('5. Voir Vos Stats')
        choice = int(input())
        if choice == 1:
            if loup['Combat'] == 1:
                print('Le village vie paisiblement, Ils vous sont redevables, mais vite d\'autres villages sont en dangers') #Si le monstre a été déjà fais il ne peut pas le refaire 
                b5()                                                                                                         # et obligé de poursuivre sa quête
            else:
                village = 'Nord'
                player_location = Nord()
                return player_location
            
        elif choice ==2 :
            if sanglier['Combat'] == 1:
                print('Le village vie paisiblement, Ils vous sont redevable, mais vite d\'autres villages sont en dangés')#Si le monstre a été déjà fais il ne peut pas le refaire 
                b5()                                                                                                         # et obligé de poursuivre sa quête
            else:
                village = 'Sud'
                player_location = Sud()
                return player_location
            
        elif choice ==3 :
            if bandits['Combat'] == 1:
                print('Le village vie paisiblement, Ils vous sont redevable, mais vite d\'autres villages sont en dangés')#Si le monstre a été déjà fais il ne peut pas le refaire 
                b5()                                                                                                        # et obligé de poursuivre sa quête
                
            else:
                village = 'Est'
                player_location = Est()
                return player_location
            
        elif choice == 4:
            if ogre['Combat'] == 1:
                print('Le village vie paisiblement, Ils vous sont redevable, mais vite d\'autres villages sont en dangés')#Si le monstre a été déjà fais il ne peut pas le refaire 
                b5()                                                                                                       # et obligé de poursuivre sa quête              
            else:
                village = 'Ouest'
                player_location = Ouest()
                return player_location
        elif choice == 5:
            print('Vous etes niveau', player['Level'])
            print('Vos points de vie sont de',player['Health'],'/', player['Max_Health'])
            print('Votre attaque est de', player['Attack'])
            print('Vous avez', player['Gold'],'d\'or')
            print('Vous avez',player['Potion'])


    else: # Si les 4 monstres envoyés son vaincu alors le boss apparaîtera sur la place.
        boss()
            
def Nord(): 

    global ennemy
    global loup

    print('\nBonjour',player['Nom'],' et bienvenue dans le nord')
    print('un loup ravage les résrve d\'un village')
    print('Trouve le loup et bat-le !')
    print('Bon courage !!')
    time.sleep(5)

    print('Bravo tu as trouvé : Le Loup')
    print('Il ne vous a pas encore vu\nVoulez vous l\'affronter ?')
    print('1. Oui\n2. Non')
    choice = int(input())
    if choice == 1:
        loup['Nom'] = 'Loup'
        loup['Attack'] = 10
        loup['Health'] = 30
        loup['Max.Health'] = 30
        loup['Experience'] = 20
        loup['Gold'] = 5
        ennemy = loup
        combat()
        return ennemy
        
        

    elif choice == 2:
        print('\nde retour à la map?')
        b5()
    combat()

def Sud():

    global sanglier
    global ennemy

    print('\nBonjour',player['Nom'],' et bienvenue dans le Sud')
    print('Un Sanglier sauvage ravage les réserves d\'un village')
    print('Trouve le Sanglier et bat-le !')
    print('Bon courage')
    time.sleep(5)


    print('Bravo tu as trouvé : Le Sanglier')
    print('Il ne vous a pas encore vu\nVoulez vous l\'affronter ?')
    print('1. Oui\n2. Non')
    choice = int(input())
    if choice == 1:
        sanglier['Nom'] = 'Sanglier'
        sanglier['level'] = 3
        sanglier['Attack'] = 20
        sanglier['Health'] = 150
        sanglier['Max.Health'] = 150
        sanglier['Experience'] = 20
        sanglier['Gold'] = 9
        ennemy = sanglier
        combat()
        return ennemy
    
    elif choice == 2:
        print('\nde retour à la map')
        b5()
    else:
        Sud()    
    combat()

                   

def Est():

    global bandits
    global ennemy

    print('\nBonjour',player['Nom'],' et bienvenue dans l\'Est')
    print('Des bandits ravage les réserve d\'un village')
    print('Trouve les bandits et bat-les !')
    print('Bon courage')
    time.sleep(5)

 

    print('/!\ Attention /!\ ')
    print('Bravoi tu as trouvé : Le Loup')
    print('Il ne vous a pas encore vu\nVoulez vous l\'affronter ?')
    print('1. Oui\n2. Non')
    choice = int(input())
    if choice == 1:

        bandits['Nom'] = 'Bandits'
        bandits['Attack'] = 17
        bandits['Health'] = 40
        bandits['Max.Health'] = 40
        bandits['Experience'] = 20
        bandits['Gold'] = 14
        ennemy = bandits
        combat()
        return ennemy

    elif choice == 2:
        print('\nde retour à la map?')
        b5()

def Ouest():

    global ogre
    global ennemy

    print('\nBonjour',player['Nom'],' et bienvenue dans l\'Ouest')
    print('un loup ravage les réserve d\'un village')
    print('Trouve le loup et bat-le !')
    print('Bon courage')
    time.sleep(5)
    
    print('/!\ Attention /!\ ')
    print('Bravo tu as trouvé : Le Loup')
    print('Il ne vous a pas encore vu\nVoulez vous l\'affronter ?')
    print('1. Oui\n2. Non')
    choice = int(input())
    if choice == 1:

        ogre['Nom'] = 'ogre'
        ogre['level'] = 1
        ogre['Attack'] = 15
        ogre['Health'] = 35
        ogre['Max.Health'] = 35
        ogre['Experience'] = 20
        ogre['Gold'] = 13
        ennemy = ogre
        combat()
        return ennemy

    elif choice == 2:
        print('\nde retour à la map?')
        b5()
    return

def combat(): 

    global Nombre_De_Combat
    global ennemy
    global player
    start = True
    phealth = player['Health'] 
    ehealth = ennemy['Health'] 
    while start == True:
        if ehealth <= 0:
            ennemy['Combat'] = ennemy['Combat'] + 1 
            start = False
            print('Vous avez battu', ennemy['Nom'], 'vous remporter', ennemy['Gold'],'gold.')
            player['Gold'] = player['Gold'] + ennemy['Gold']
            player['Experience'] = player['Experience'] + ennemy['Experience']
            if player['Experience'] >= player['Experienceneed']:
                player['Level'] = player['Level'] + 1
                print('Vous avez gagné un niveau, vous etes maintenant niveau', player['Level'])
                print('Vous avez gagné', ennemy['Experience'],'.' )

                findecombat()

        elif phealth  <= 0:
            start = False
            print('Vous avez été vaincu')
            mort()

        else: 
            print('Que Voulez-vous faire ')
            print('1. Attaquer')
            print('2. Boire une potion')
            print('3. Fuire')
            choice = int(input())
            if choice == 1:
                print('Vous retirer', player['Attack'])
                print('Il reste', ennemy['Health'], '/', ennemy['Max.Health'],'HP')
                ehealth = ehealth - player['Attack']

            elif choice == 2:
                if player['Potion'] == 0:
                    print('vous n\'avez pas assez de potion')
                else:
                    print('Vous buvez une potion')
                    player['Health'] = player['Health'] + 30
                    if player['Health'] > 100:
                        player['Health'] = 100
                        combat()

            print(ennemy['Nom'], ' vous attaque et vous retire',ennemy['Attack'],' points de vie')
            player['Health'] = player['Health'] - ennemy['Attack']
            print('Il vous reste', player['Health'], '/', player['Max_Health'],'HP')
            
    Nombre_De_Combat = Nombre_De_Combat + 1

    return player,

def findecombat(): # A chaque fin de combat ( exepté pour le boss ) les villageois commerceront avec l'aventurier

    global village

    print('Félicitation, vous avez térasser le', ennemy['Nom'],'qui térrorisais ....')
    print('Des commerçants vous porposes de rentrer dans leur magasins afin d\'acheter des armes / potions a prix réduit')
    print('Voulez-vous faire un tour ? ')
    print('1. Oui')
    print('2. Non')
    choice = int(input())
    if choice == 1:
        print('Bonjour, chère aventurier. Que voulez-vous acheter')
        shop()
    elif choice == 2:
        b5()
    else:
        findecombat()

def shop(): # Magasin
    
    print('1. Potion pour le prix de 3')
    print('2. Armes')
    print('3. Retour a la place')
    choice = int(input())
    if choice == 1:
        if player['Gold'] < 3:
            print('Vous n\'avez pas assez d\'or')
            shop()
        else:    
            print('Vous avez acheté une petite potion')
            player['Potion'] = player['Potion'] + 1
            player['Gold'] = player['Gold'] - 3
            print('Voulez-vous en acheter d\'autres ?')
            choicepotion = int(input())
            if choicepotion == 1:
                shop()

    elif choice == 2:
        print('1. épée en bois pour le prix de 10')
        print('2. épée en pierre pour le prix de 30')
        print('3. épée en fer pour le prix de 40')
        print('4. épée en or pour le prix de 50')
        print('5. épée enchanté pour le prix de 60')
        if choice == 1:
            if player['Gold'] < 3:
                print('Vous n\'avez pas assez d\'or')
                shop()
            else:
                print('Vous avez acheté une épée en bois pour 10')
                player['Attack'] = player['Defaultatk'] + 3

        elif choice == 2:
            if player['Gold'] < 3:
                print('Vous n\'avez pas assez d\'or')
                shop()
            else:
                print('Vous avez acheté une épée en pierre pour 30')
                player['Attack'] = player['Defaultatk'] + 5

        elif choice == 3:
            if player['Gold'] < 3:
                print('Vous n\'avez pas assez d\'or')
                shop()
            else:
                print('Vous avez acheté une épée en fer pour 40')
                player['Attack'] = player['Defaultatk'] + 7

    elif choice == 4:
        if player['Gold'] < 3:
            print('Vous n\'avez pas assez d\'or')
            shop()
        else:
            print('Vous avez acheté une épée en or pour 50')
            player['Attack'] = player['Defaultatk'] + 10
    elif choice == 5:
        if player['Gold'] < 3:
            print('Vous n\'avez pas assez d\'or')
            shop()
        else:
            print('Vous avez acheté une épée enchanté pour 60 ')
            player['Attack'] = player['Defaultatk'] + 15
    elif choice == 3:
        b5()
    else:
        shop()

    b5()
    return player


def boss(): # Boss

    global player
    start = True

    Frankenstein = {}
    Frankenstein['Nom'] = 'Frankenstein'
    Frankenstein['Attack'] = 30
    Frankenstein['Health'] = 150
    Frankenstein['Max.Health'] = 100
    Frankenstein['Experience'] = 100
    Frankenstein['Gold'] = 100
    phealth = player['Health'] 
    bhealth = Frankenstein['Health'] 

    print('/!\ Attention /!\ ')
    print('Vous vous trouvez actuellement devant le boss : Frankenstein')
    print('Il ne vous a pas encore vu\nVoulez vous l\'affronter ?')
    print('1. Oui\n2. Non')
    choice = int(input())
    if choice == 1:

        while start:

            if bhealth <= 0:
                start = False
                print('Vous avez battu', Frankenstein['Nom'], 'vous remporter', Frankenstein['Gold'],'gold.')
                player['Gold'] = player['Gold'] + Frankenstein['Gold']
                player['Experience'] = player['Experience'] + Frankenstein['Experience']
                if player['Experience'] >= player['Experienceneed']:
                    player['Level'] = player['Level'] + 1
                    print('Vous avez gagné un niveau, vous etes maintenant niveau', player['Level'])
                    print('Vous avez gagné', Frankenstein['Experience'],'.' )

            elif phealth < 0:
                start = False
                print('Vous avez été vaincu')  
            else: 
                print('Que Voulez-vous faire ')
                print('1. Attaquer')
                print('2. Boire une potion')
                print('3. Fuir')
                choice = int(input())
                if choice == 1:
                    print('Vous retirer', player['Attack'])
                    print('Il reste', Frankenstein['Health'], '/', Frankenstein['Max.Health'],'HP')
                    bhealth = bhealth - player['Attack']

                elif choice == 2:
                    if player['Potion'] == 0:
                        print('vous n\'avez pas assez de potion')
                    else:
                        print('Vous buvez une potion')
                        player['Health'] = player['Health'] + 30
                        if player['Health'] > 100:
                            player['Health'] = 100
                            boss()
                elif choice == 3:
                    print('Vous ne pouvez pas fuir')

                print(Frankenstein['Nom'], ' vous attaque et vous retire',Frankenstein['Attack'],' points de vie')
                player['Health'] = player['Health'] - Frankenstein['Attack']
                print('Il vous reste', player['Health'], '/', player['Max_Health'],'HP')
    else:
        combat()

    print('Félicitation vous avez vaincu Frankenstein, \nvous avez rapporté la paix dans les villages situé dans les quatres coins cardinaux')
    print('Credits:\nMorad Zerouali\nMehdi Zerouali\nYanis Fallard')

def mort():
    print('Vous avez failli a votre mission')
    print('Voulez-vous recommencer ?')
    print('1. Oui')
    print('2. Non')
    choice = int(input())
    if choice == 1:
        main()
    elif choice == 2:
        sys.exit()
    else:
        mort()
    
main()

