def fusion(tab1: list, tab2: list) -> list:
    listeFinal = []
    while tab1 != [] and tab2 != []:
        if tab1[0] < tab2[0]:
            listeFinal.append(tab1.pop(0))
        else:
            listeFinal.append(tab2.pop(0))
    if not tab1:
        for i in tab2:
            listeFinal.append(i)
    else:
        for i in tab1:
            listeFinal.append(i)
    return listeFinal


print(fusion([3, 5], [2, 5]))


def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    romains = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(nombre) == 1:
        return romains[nombre[0]]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return ...

print(traduire_romain("XIV"))
nombre = [1,2,3]
print(nombre[:1])