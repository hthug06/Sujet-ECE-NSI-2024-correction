def ou_exclusif(tab1, tab2):
    tabFinal = []
    for i in range(len(tab1)):
        if tab1[i] == 0 and tab2[i] == 0:
            tabFinal.append(0)
        if tab1[i] == 1 and tab2[i] == 0:
            tabFinal.append(1)
        if tab1[i] == 0 and tab2[i] == 1:
            tabFinal.append(1)
        if tab1[i] == 1 and tab2[i] == 1:
            tabFinal.append(0)

    return tabFinal

print( ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]))
print( ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]))


class Carre:
    def __init__(self, liste, n): 
        self.ordre = n        
        self.tableau = [[liste[i + j * n] for i in range(n)] 
                        for j in range(n)] 
                                   
    def affiche(self):        
        '''Affiche un carré''' 
        for i in range(self.ordre): 
            print(self.tableau[i]) 
                                   
    def somme_ligne(self, i): 
        '''Calcule la somme des valeurs de la ligne i''' 
        somme = 0             
                                   
        for j in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
    def somme_col(self, j):   
        '''Calcule la somme des valeurs de la colonne j''' 
        somme = 0
                                   
        for i in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
                                   
    def est_semimagique(self): 
        s = self.somme_ligne(0) 
        #test de la somme de chaque ligne 
        for i in range(len(self.tableau)):
            if self.somme_ligne(i) != s:
                return False
                                   
        #test de la somme de chaque colonne 
        for j in range(len(self.tableau)):
            if self.somme_col(j) != s:
                return False
                                   
        return True

print("")
print("CARRE c3")
lst_c3 = [3, 4, 5, 4, 4, 4, 5, 4, 3]
c3 = Carre(lst_c3, 3)
c3.affiche()
print(c3.est_semimagique())

print("CARRE c2")
lst_c2 = [1, 7, 7, 1]
c2 = Carre(lst_c2, 2)
c2.affiche()
print(c2.est_semimagique())

print("CARRE c3Bis")
lst_c3Bis = [2, 9, 4, 7, 0, 3, 6, 1, 8]
c3Bis = Carre(lst_c3Bis, 3)
c3Bis.affiche()
print(c3Bis.est_semimagique())

