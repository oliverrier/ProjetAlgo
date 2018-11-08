def det2(mat):
    #Test si la matrice est une matrice carré de taille 2
    if len(mat)!=2 or len(mat[0])!=2 or len(mat[1])!=2:
        return 'error'
    #Calcul a*d
    a=mat[0][0]*mat[1][1]
    #Calcul b*c
    b=mat[0][1]*mat[1][0]
    #Calcul déterminant
    determinant2=abs(a-b)
    return determinant2
    
print(det2([[-3,4],[0,1]]))
