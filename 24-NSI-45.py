def compte_occurrences(x, tab):
    nbr_occurence = 0
    for elt in tab:
        if elt == x:
            nbr_occurence+=1
    return nbr_occurence

print( compte_occurrences(5, []))
print( compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]))
print( compte_occurrences('a', ['a','b','c','a','d','e','a']))

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = []
    a_rendre = somme_versee-somme_due
    i = len(pieces) - 1
    while a_rendre > 0:
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(pieces[i])
        a_rendre = a_rendre-pieces[i]
    return rendu


print(rendu_monnaie(700, 700))
print(rendu_monnaie(102, 500))