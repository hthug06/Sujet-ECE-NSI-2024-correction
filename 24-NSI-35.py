def annee_temperature_minimale(tabtemp, tabannnee):
    mini = 0
    temp_min = tabtemp[0]
    for i in range(len(tabannnee)):
        if temp_min > tabtemp[i]:
            temp_min = tabtemp[i]
            mini = i
    return tabtemp[mini], tabannnee[mini]


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
print(annee_temperature_minimale(t_moy, annees))


def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat


def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return inverse == chaine


def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine = str(nbre)
    return est_palindrome(chaine)

print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))