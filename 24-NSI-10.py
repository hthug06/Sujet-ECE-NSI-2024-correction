def moyenne(tab):
    sommede0 = 0
    for i in range(len(tab)):
        if tab[i][1] != 0:
            sommede0 += 1
        else:
            None
    if sommede0 == 0:
        return None

    somme = 0
    coeffPourDiviser = 0
    for j in tab:
        somme += j[0] * j[1]
        coeffPourDiviser += j[1]
    return somme / coeffPourDiviser


print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))

coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]


def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par 
        des "*" , les 0 par un espace " " '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)


def liste_zoom(liste_depart, k):
    '''renvoie une liste contenant k fois chaque élément de
       liste_depart'''
    liste_zoomee = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoomee.append(elt)
    return liste_zoomee


def dessin_zoom(grille, k):
    '''renvoie une grille où les lignes sont zoomées k fois
       ET répétées k fois'''
    grille_zoomee = []
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne, k)
        for i in range(k):
            grille_zoomee.append(ligne_zoomee)
    return grille_zoomee


print(affiche(coeur))
affiche(dessin_zoom(coeur, 2))
print(liste_zoom([1, 2, 3], 3))
