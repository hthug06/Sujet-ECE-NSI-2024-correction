class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit


def taille(a):
    if a is None:
        return 0
    else:
        return 1 + taille(a.gauche) + taille(a.droit)


def hauteur(a):
    if a is None:
        return -1
    else:
        return 1 + max(hauteur(a.gauche), hauteur(a.droit))


# Exemple d'arbre binaire
a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

# Test des fonctions
print(hauteur(a))
print(taille(a))
print(hauteur(None))
print(taille(None))
print(hauteur(Noeud(1, None, None)))
print(taille(Noeud(1, None, None)))


def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i]
    tab_ins[indice] = element
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i - 1]
    return tab_ins


print(ajoute(1, 4, [7, 8, 9]))
print( ajoute(3, 4, [7, 8, 9]))
print( ajoute(0, 4, [7, 8, 9]))
