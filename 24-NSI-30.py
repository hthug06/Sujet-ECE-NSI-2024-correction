def fusion(tab1:list, tab2:list) -> list:
    listeFinal = []
    for i in range(len(tab1)+len(tab2)-2):
        if tab1[i] < tab2[i]:
            listeFinal.append(tab1[i])
        else:
            listeFinal.append(tab2[i])
    return listeFinal
print(fusion([3, 5], [2, 5]))

def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return ... 
    elif romains[nombre[0]] >= ...: 
        return romains[nombre[0]] + ... 
    else:
        return ... 


