def occurrences(caractere, chaine):
    nbr = 0
    for ch in chaine:
        if ch == caractere:
            nbr+=1
    return nbr

print(occurrences('e', "sciences"))
print(occurrences('i',"mississippi"))
print(occurrences('a',"mississippi"))

valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return [1]
    v = valeurs[rang]
    if v <= a_rendre:
        return [v ]+ rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, rang+1)

print(rendu_glouton(67, 0))
print(rendu_glouton(291, 0))
print(rendu_glouton(291,1))


