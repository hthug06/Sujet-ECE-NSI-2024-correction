from random import randint

def tri_selection(liste : list):
    for i in range(len(liste)):

        petit = liste[i]
        for j in range(i+1):
            if j < petit:
                petit = j

        temp =



def plus_ou_moins():
    nb_mystere = randint(1, ...) 
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = ... 

    while nb_mystere != ... and compteur < ...: 
        compteur = compteur + 1
        if nb_mystere ... nb_test: 
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", ...) 
        print("Nombre d'essais: ", ...) 
    else:
        print ("Perdu ! Le nombre était ", ...) 

