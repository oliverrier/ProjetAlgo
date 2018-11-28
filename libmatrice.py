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
La fonction det2(mat) permet d'obtenir le déterminant de la matrice 2x2 mat passée en paramètre,
Pour se faire, on vérifie si la matrice est bien une matrice 2x2, 
Si on a bien une matrice 2x2 de la forme: [[a,b],[c,d]] alors le calcul du déterminant s'effectue
de la façon suivante : det(mat)=a*d-(c*b).
'''


def det2(mat):
    #Test si la matrice est une matrice carré de taille 2
    if len(mat) != 2 or len(mat[0]) != 2 or len(mat[1]) != 2:
        return 'error'
    #Calcul a*d
    a = mat[0][0] * mat[1][1]
    #Calcul b*c
    b = mat[0][1] * mat[1][0]
    #Calcul déterminant
    determinant2 = a - b
    return determinant2


def reduit(mat,ligne,colonne):
    mat2 = [[0,0],[0,0]]
    ml = 0
    for l in range (0,3):
        if l != ligne:
            mc = 0
            for c in range (0,3):
                if c != colonne:
                    mat2[ml][mc] = mat[l][c]
                    mc += 1
            ml += 1
    return mat2



'''
La fonction det3(mat) permet d'obtenir le déterminant de la matrice 3x3 passée en paramètre,
Pour se faire, on vérifie si la matrice est bien une matrice 3x3,
Si on a bien une matrice 3x3 de la forme mat=[[a,b,c],[d,e,f],[g,h,i]]
avec :
    - a accessible par la clé mat[0][0]
    - b accessible par la clé mat[0][1]
    - c accessible par la clé mat[0][2]
    - d accessible par la clé mat[1][0]
    - e accessible par la clé mat[1][1]
    - f accessible par la clé mat[1][2]
    - g accessible par la clé mat[2][0]
    - h accessible par la clé mat[2][1]
    - i accessible par la clé mat[2][2]
La formule pour calculer le déterminant d'une matrice 3x3 étant:
On utilise également la fonction reduit(mat,ligne,colonne) afin d'obtenir la matrice 2x2 nous
permettant de calculer son déterminant.

'''
def det3(mat):
    #Condition taille 
    if len(mat)!=3 or len(mat[0])!=3 or len(mat[1])!=3 or len(mat[2])!=3:
        return 'error'
    determ3 = mat[0][0] * det2(reduit(mat,0,0)) - mat[0][1] * det2(reduit(mat,0,1)) + mat[0][2] * det2(reduit(mat,0,2))
    return determ3



def inverse(mat):
    transpose_comatrice = transpose(comatrice(mat))
    for i in range (0,3):
        for j in range (0,3):
            transpose_comatrice[i][j] = transpose_comatrice[i][j] / det3(mat)
    return transpose_comatrice
    


def transpose(mat):
    transpose=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,3):
        for j in range(0,3):
            transpose[j][i]=mat[i][j]
    return transpose


def comatrice(mat):
    comatrice = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range (0,3):
        for j in range (0,3):
            comatrice[i][j] = (-1)**(i+j)*det2(reduit(mat,i,j)) 
    return comatrice
            
