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
