def renverse(ch):
    return ch[::-1]

print( renverse(""))
print(renverse("abc"))
print(renverse("informatique"))

def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = 2*i
            while multiple < n:
                tab[multiple] = False
                multiple = multiple+i
    return premiers

print( crible(40))


