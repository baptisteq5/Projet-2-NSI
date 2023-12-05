def monnaie_librairie(monnaie_a_rendre):
    rendre = monnaie_a_rendre
    liste_monnaie = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    billets = []
    euro = liste_monnaie[len(liste_monnaie) - 1]
    while rendre > 0:
        if euro <= rendre:
            billets.append(euro)
            rendre -= euro
        else:
            del liste_monnaie[len(liste_monnaie) - 1]
            euro = liste_monnaie[len(liste_monnaie) - 1]
    return billets
