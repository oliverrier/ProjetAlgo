'''
Cette librairie a été créée afin d'inverser une matrice 3x3.
Pour cela elle va utiliser plusieurs fonctions lui permettant de calculer cet inverse.
Elle utilisera des fonctions permettant de calculer:
    - le déterminant d'une matrice 2x2 appelée det2(mat)
    - le déterminant d'une matrice 3x3 appelée det3(mat)
    - la matrice 2x2 issue d'une matrice 3x3 réduite appelée reduit(mat,ligne,colonne)
    - la comatrice d'une matrice appelée comatrice(mat)
    - la transposée d'une matrice appelée transposée(mat)
    - l'inverse d'une matrice appelée inverse(mat)
'''

'''
La fonction det2(mat) permet d'obtenir le déterminant de la matrice 2x2 mat passée en parmètre,
Pour se faire 

'''


def det2(mat):
    #Test si la matrice est une matrice carré de taille 2
    if len(mat) != 2 or len(mat[0]) != 2 or len(mat[1]) != 2:
        return 'error'
    #Calcul a*d
    a=mat[0][0] * mat[1][1]
    #Calcul b*c
    b=mat[0][1] * mat[1][0]
    #Calcul déterminant
    determinant2 = a - b
    return determinant2


'''
La fonction det3(mat)
'''
