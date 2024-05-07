def multiplication(n1: int, n2: int) -> int:
    somme = 0
    if n1 < 0 and n2 < 0:
        for i in range(n1, 0):
            somme += n2
    elif n1 > 0 and n2 > 0:
        for i in range(n1):
            somme += n2
    elif n1 < 0 < n2:
        for i in range(n1, 0):
            somme += n2
    elif n1 > 0 > n2:
        for i in range(n1):
            somme += n2

    return somme


print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))


def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, m+1, j)
    elif tab[m] > x:
        return chercher(tab, x, i, m-1)
    else:
        return m


print("")
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print( chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))
