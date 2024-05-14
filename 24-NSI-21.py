def recherche_motif(motif, texte):
    tab = []
    state = False
    for i in range(len(texte)-1):
        state = False
        for j in range(len(motif)):
            if texte[i+j] == motif[j]:
                state = True
            else:
                state = False
                break
        if state == True:
            tab.append(i)
    return tab

print(recherche_motif("ab", ""))
print( recherche_motif("ab", "cdcdcdcd"))
print( recherche_motif("ab", "abracadabra"))
print(recherche_motif("ab", "abracadabraab"))

def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    """if x ...: 
        acc.append(x)
        for y in ...: 
            parcours(adj, ...) """

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, ...) 
    return acc


