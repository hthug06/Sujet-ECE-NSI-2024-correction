a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'], \
     'C': ['', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'], \
     'H': ['', '']}


def taille(graph, depart):
    if graph[depart][0] == '' and graph[depart][1] == '':
        return 1
    elif graph[depart][0] != '' and graph[depart][1] == '':
        return 1 + taille(graph, graph[depart][0])
    elif graph[depart][0] == '' and graph[depart][1] != '':
        return 1 + taille(graph, graph[depart][1])
    else:
        return 1 + taille(graph, graph[depart][0]) + taille(graph, graph[depart][1])


print(taille(a, 'F'))
print(taille(a, 'B'))
print(taille(a, 'I'))


def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j] 
    tab[j] = temp 
    return tab

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N): 
        imin = k 
        for i in range(k, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin) 
    return tab

print(echange([1,2,3,4], 1, 2))
print(tri_selection([1,7,5,4,0,8]))


