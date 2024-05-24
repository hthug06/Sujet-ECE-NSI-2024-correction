from random import randint


def ajoute_dictionnaires(d1, d2):
    dicofinal = {}
    for key in d1:
        if key in d2:
            dicofinal[key] = d1[key] + d2[key]
        else:
            dicofinal[key] = d1[key]

    for key in d2:
        if key in d1:
            dicofinal[key] = d1[key] + d2[key]
        else:
            dicofinal[key] = d2[key]
    return dicofinal


print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))

a = [True, True, False]
print(sum(a))
def nombre_coups():
    '''Simule un jeu de plateau avec 12 cases et renvoie le nombre
    minimal de coups pour visiter toutes les cases.'''
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [False] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = 0
    while sum(cases_vues) < 12:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % 12
        if not cases_vues[case_en_cours]:
            cases_vues[case_en_cours] = True
            nombre_cases_vues = nombre_cases_vues+1
        n = n+1
    return n

print(nombre_coups())
