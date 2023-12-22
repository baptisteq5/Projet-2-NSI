def monnaie_librairie(monnaie_a_rendre):
    liste_monnaie = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    billets = []
    euro = liste_monnaie[len(liste_monnaie) - 1]
    while monnaie_a_rendre > 0:
        if euro <= monnaie_a_rendre:
            billets.append(euro)
            monnaie_a_rendre -= euro
        else:
            del liste_monnaie[len(liste_monnaie) - 1]
            euro = liste_monnaie[len(liste_monnaie) - 1]
    return billets

def monnaie_vetements(monnaie_a_rendre):
    liste_monnaie = [200, 100, 100, 100, 50, 20, 10, 5, 2, 2, 2, 2, 2]
    billets = []
    while monnaie_a_rendre > 0 and liste_monnaie:
        euro = liste_monnaie[0]
        reste = sum(liste_monnaie) - euro
        if euro <= monnaie_a_rendre or reste < monnaie_a_rendre:
            billets.append(euro)
            monnaie_a_rendre -= euro
        del liste_monnaie[0]
    rendu_en_trop = -1*monnaie_a_rendre
    return (billets, rendu_en_trop)

def monnaie_baguette(gallions: int, mornilles: int, noises: int):
    assert type(gallions) == int, "Le paramètre gallions doit être un entier"
    assert type(mornilles) == int, "Le paramètre mornilles doit être un entier"
    assert type(noises) == int, "Le paramètre noises doit être un entier"
    total_noises = noises + 29 * mornilles + 493 * gallions
    a_rendre = {'gallions': 0, 'mornilles': 0, 'noises': 0}
    while total_noises >= 493:
        a_rendre['gallions'] += 1
        total_noises -= 493
    while total_noises >= 29:
        a_rendre['mornilles'] += 1
        total_noises -= 29
    a_rendre['noises'] += total_noises
    return a_rendre

def librairie():
    print('Bienvenue chez Fleury & Bott, libraire!')
    sommes_preenregistrees = [0, 60, 63, 231, 899]
    rester = True
    while rester:
        type_rendu = input('Voulez vous: \
                           \n1: choisir la somme à rendre\
                           \n2: exécuter avec les sommes préenregistrées\
                           \nToute autre réponse sort de la boutique: ')
        if type_rendu == '1':
            monnaie_a_rendre = int(input('Saisissez la somme à rendre: '))
            resultat = monnaie_librairie(monnaie_a_rendre)
            print(f'Pour la somme {monnaie_a_rendre}, le libraire vous rend ces espèces: {resultat}')
        elif type_rendu == '2':
            for somme in sommes_preenregistrees:
                resultat = monnaie_librairie(somme)
                print(f'Pour la somme {somme}, le libraire vous rend ces espèces: {resultat}')
        else:
            rester = False
    print('Vous êtes sorti de la librarie! Au revoir!')
            
def vetements():
    print('Bienvenue chez Mme Guipure, boutique de prêt-à-porter!')
    sommes_preenregistrees = [0, 17, 68, 231, 497, 842]
    rester = True
    while rester:
        type_rendu = input('Voulez vous: \
                           \n1: choisir la somme à rendre\
                           \n2: exécuter avec les sommes préenregistrées\
                           \nToute autre réponse sort de la boutique: ')
        if type_rendu == '1':
            monnaie_a_rendre = int(input('Saisissez la somme à rendre: '))
            resultat = monnaie_vetements(monnaie_a_rendre)
            print(f'Pour la somme {monnaie_a_rendre}, Mme Guipure vous rend ces espèces: {resultat[0]}')
            if resultat[1] > 0:
                print(f"Madame Guipure n'a pas réussi à vous rendre la somme exacte alors elle vouds a rendu {resultat[1]} en trop!")
            if resultat[1] < 0:
                print(f"Madame Guipure n'a pas réussi à tout vous rendre, il manque {resultat[1]}!")
        elif type_rendu == '2':
            for somme in sommes_preenregistrees:
                resultat = monnaie_vetements(somme)
                print(f'Pour la somme {somme}, Mme Guipure vous rend ces espèces: {resultat[0]}')
                if resultat[1] > 0:
                    print(f"Madame Guipure n'a pas réussi à vous rendre la somme exacte alors elle vouds a rendu {resultat[1]} en trop!")
                if resultat[1] < 0:
                    print(f"Madame Guipure n'a pas réussi à tout vous rendre, il manque {resultat[1]}!")
        else:
            rester = False
    print('Vous êtes sorti de la boutique de prêt-à-porter! Au revoir!')
                
def baguettes():
    print('Bienvenue chez Ollivander, fabriquant de baguettes magiques!')
    sommes_preenregistrees = [(0, 0, 0), (0, 0, 654), (0, 23, 78), (2, 11, 9), (7, 531, 451)]
    rester = True
    while rester:
        type_rendu = input('Voulez vous: \
                           \n1: choisir la somme à rendre\
                           \n2: exécuter avec les sommes préenregistrées\
                           \nToute autre réponse sort de la boutique: ')
        if type_rendu == '1':
            gallions_a_rendre = int(input('Saisissez le nombre de gallions à rendre: '))
            mornilles_a_rendre = int(input('Saisissez le nombre de mornilles à rendre: '))
            noises_a_rendre = int(input('Saisissez le nombre de noises à rendre: '))
            monnaie_a_rendre = (gallions_a_rendre, mornilles_a_rendre, noises_a_rendre)
            resultat = monnaie_baguette(monnaie_a_rendre[0], monnaie_a_rendre[1], monnaie_a_rendre[2])
            print(f'Pour la somme {monnaie_a_rendre}, le baguettier vous rend ces espèces: {resultat}')
        elif type_rendu == '2':
            for somme in sommes_preenregistrees:
                resultat = monnaie_baguette(somme[0], somme[1], somme[2])
                print(f'Pour la somme {somme}, le baguettier vous rend ces espèces: {resultat}')
        else:
            rester = False
    print('Vous êtes sorti de la boutique de baguettes! Au revoir!')



def ihm():
    print('Bienvenue sur le chemin de traverse! ')
    rester = True
    
    while rester:
        boutique = input('Dans quelle boutique voulez-vous aller? \
                         \n1: Librairie de Fleury & Bott\
                         \n2: Prêt à porter de Madame Guipure\
                         \n3: Ollivander fabriquant de baguettes\
                         \nToute autre réponse quitte le chemin de traverse: ')
        if boutique == '1':
            librairie()
        elif boutique == '2':
            vetements()
        elif boutique == '3':
            baguettes()
        else:
            rester = False
    print('Vous avez quitté le chemin de traverse! A une prochaine fois!')
            
ihm()
