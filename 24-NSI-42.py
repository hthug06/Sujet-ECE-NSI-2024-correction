def moyenne(tab):
    somme = 0
    for nbr in tab:
        somme+=nbr
    return float(somme/len(tab))

print(moyenne([1]))
print(moyenne([1, 2, 3, 4, 5, 6, 7]))
print(moyenne([1, 2]))

def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""

    debut = 0
    fin = len(tab)-1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = debut+1
        else:
            fin = fin-1
    return False

print( dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print( dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))
print( dichotomie([], 28))


