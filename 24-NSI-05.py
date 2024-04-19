def max_et_indice(tab: list):
    indice = 0
    maximum = tab[0]
    for i in range(len(tab)):
        if maximum < tab[i]:
            maximum = tab[i]
            indice = i
    return maximum, indice


print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))
print(max_et_indice([-1, -1, 3, 3, 3]))
print(max_et_indice([1, 1, 1, 1]))


def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = []

    for x in tab:
        if x < 1 or x > len(tab) or type(x) != int:
            return False
        vus.append(x)
    return True


print(est_un_ordre([1, 6, 2, 8, 3, 7]))
print(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]))


def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente 
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre) != False, "doit petre un ordre"
    n = len(ordre)
    nb = 0
    if ordre[0] != 1:  # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < n - 1:
        # print(i)
        if ordre[i] - ordre[i + 1] not in [-1, 1]:  # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[len(ordre) - 1] != n:  # le dernier n'est pas n
        nb = nb + 1
    return nb


print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))
print(nombre_points_rupture([1, 2, 3, 4, 5]))
