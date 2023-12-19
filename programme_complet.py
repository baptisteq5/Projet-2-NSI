def librairie():
    print('Bienvenue chez Fleury & Bott, libraire!')
    sommes_preenregistrees = [0, 60, 63, 231, 899]
    rester = True
    while rester:
        type_rendu = input('voulez vous: \
                           \n1: choisir la somme à rendre\
                           \n2: exécuter avec les sommes préenregistrées\
                           \nToute autre réponse sort de la boutique: ')
        if type_rendu == 1:
            monnaie_a_rendre = input('saisissez la somme à rendre: ')
            resultat = monnaie_librairie(monnaie_a_rendre)
            print(f'pour la somme {monnaie_a_rendre}, le libraire vous rend\
                  ces espèces: {resultat}')
        elif type_rendu == 2:
            for somme in sommes_preenregistrees:
                resultat = monnaie_librairie(somme)
                print(f'pour la somme {somme}, le libraire vous rend \
                      ces espèces: {resultat}')
        else:
            rester = False
            
def vetements():
    print('Bienvenue chez Mme Guipure, boutique de prêt-à-porter!')
    sommes_preenregistrees = [0, 17, 68, 231, 497, 842]
    rester = True
    while rester:
        type_rendu = input('voulez vous: \
                           \n1: choisir la somme à rendre\
                           \n2: exécuter avec les sommes préenregistrées\
                           \nToute autre réponse sort de la boutique: ')
        if type_rendu == 1:
            monnaie_a_rendre = input('saisissez la somme à rendre: ')
            resultat = monnaie_vetements(monnaie_a_rendre)
            print(f'pour la somme {monnaie_a_rendre}, Mme Guipure vous rend\
                  ces espèces: {resultat[0]}')
            if resultat[1] > 0:
                print(f"Madame Guipure n'a pas réussi à vous rendre la somme \
                      exacte alors elle vouds a rendu {resultat[1]} en trop!")
            if resultat[1] < 0:
                print(f"Madame Guipure n'a pas réussi à tout vous rendre, il manque {resultat[1]}!")
        elif type_rendu == 2:
            for somme in sommes_preenregistrees:
                resultat = monnaie_vetements(somme)
                print(f'pour la somme {somme}, Mme Guipure vous rend \
                      ces espèces: {resultat[0]}')
                if resultat[1] > 0:
                    print(f"Madame Guipure n'a pas réussi à vous rendre la somme \
                          exacte alors elle vouds a rendu {resultat[1]} en trop!")
                if resultat[1] < 0:
                    print(f"Madame Guipure n'a pas réussi à tout vous rendre, il manque {resultat[1]}!")
        else:
            rester = False
                
def baguettes():
    print('Bienvenue chez Ollivander, fabriquant de baguettes magiques!')
    sommes_preenregistrees = [(0, 0, 0), (0, 0, 654), (0, 23, 78), (2, 11, 9), (7, 531, 451)]
    rester = True
    while rester:
        type_rendu = input('voulez vous: \
                           \n1: choisir la somme à rendre\
                           \n2: exécuter avec les sommes préenregistrées\
                           \nToute autre réponse sort de la boutique: ')
        if type_rendu == 1:
            gallions_a_rendre = input('saisissez le nombre de gallions à rendre: ')
            mornilles_a_rendre = input('saisissez le nombre de mornilles à rendre: ')
            noises_a_rendre = input('saisissez le nombre de noises à rendre: ')
            monnaie_a_rendre = (gallions_a_rendre, mornilles_a_rendre, noises_a_rendre)
            resultat = monnaie_baguette(monnaie_a_rendre)
            print(f'pour la somme {monnaie_a_rendre}, le baguettier vous rend\
                  ces espèces: {resultat}')
        elif type_rendu == 2:
            for somme in sommes_preenregistrees:
                resultat = monnaie_baguette(somme)
                print(f'pour la somme {somme}, le baguettier vous rend \
                      ces espèces: {resultat}')
        else:
            rester = False



def ihm():
    print('Bienvenue sur le chemin de traverse! ')
    rester = True
    
    while rester:
        boutique = input('Dans quelle boutique voulez-vous aller? \
                         \n1: Librairie de Fleury & Bott\
                         \n2: Prêt à porter de Madame Guipure\
                         \n3: Ollivander fabriquant de baguettes\
                         \nToute autre réponse quitte le chemin de traverse: ')
        if boutique == 1:
            librairie()
        elif boutique == 2:
            vetements()
        elif boutique == 3:
            baguettes()
        else:
            rester = False
            
