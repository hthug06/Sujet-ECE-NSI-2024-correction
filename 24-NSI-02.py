def correspond(mot, mot_a_trou):
    etat = True
    if len(mot) != len(mot_a_trou):
        etat = False
        return etat
    print(etat)
    for i in range(len(mot)):
        if mot_a_trou[i] != "*" and mot[i] == mot_a_trou[i] or mot_a_trou[i] == "*":
            None
        else:
            etat = False
        print(etat, mot_a_trou[i], mot[i])
    return etat


print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))


def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et
    False sinon.'''
    expediteur = 'A'
    destinataire = plan['A']
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires = nb_destinataires + 1

    return nb_destinataires == len(plan)


plan_a = {'A': 'E', 'B': 'F', 'C': 'D', 'D': 'C', 'E': 'B', 'F': 'A'}
plan_b = {'A': 'C', 'B': 'F', 'C': 'E', 'D': 'A', 'E': 'B', 'F': 'D'}

print(est_cyclique(plan_a))
print(est_cyclique(plan_b))
