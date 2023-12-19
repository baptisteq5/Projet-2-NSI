def monnaie_vetements(monnaie_a_rendre):
    liste_monnaie = [200, 100, 100, 100, 50, 20, 10, 5, 2, 2, 2, 2, 2]
    billets = []
    while monnaie_a_rendre > 0 and liste_monnaie:
        euro = liste_monnaie[0]
        if monnaie_a_rendre == 1:
            billets.append(liste_monnaie[len(liste_monnaie) - 1])
            monnaie_a_rendre -= liste_monnaie[len(liste_monnaie) - 1]
            liste_monnaie.pop
        elif monnaie_a_rendre <= 10 and monnaie_a_rendre % 2 == 0 and euro <10 and euro == 5:
            pass
        elif euro <= monnaie_a_rendre:
            billets.append(euro)
            monnaie_a_rendre -= euro
        del liste_monnaie[0]
    rendu_en_trop = -1*monnaie_a_rendre
    return (billets, rendu_en_trop)
