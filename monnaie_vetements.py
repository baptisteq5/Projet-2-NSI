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

print(monnaie_vetements(256))
