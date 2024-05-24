def parcours_largeur(abr):
    if abr is None:
        return []

    queue = [abr]
    result = []

    while queue:
        noeud = queue.pop(0)
        g, x, d = noeud
        result.append(x)

        if g is not None:
            queue.append(g)
        if d is not None:
            queue.append(d)

        print(queue)

    return result


# Exemple d'utilisation
arbre = (((None, 1, None), 2, (None, 3, None)),
         4,
         ((None, 5, None), 6, (None, 7, None)))

print(parcours_largeur(arbre)) # Merci chat GPT

def somme_max(tab):
    n = len(tab)
    sommes_max = [0] * n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1, n):
        if ... + ... > ...:
            sommes_max[i] = ...
        else:
            sommes_max[i] = ...
            # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if ... > ...:
            maximum = i

    return sommes_max[...]
