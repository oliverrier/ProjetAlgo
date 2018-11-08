mat = [[-3,-3,-4],[0,1,1],[4,3,4]] #Création de la matrice





def reduit(mat,ligne,colonne):
    mat2 = [[0,0],[0,0]]
# La fonction va parcourir la matrice, I verticalement et J horizontalement.
    ml = 0
    for i in range 3:
        mc = 0
        if i != ligne:
        for j in range 3:
            if j != colonne:
                mat2[ml],[mc] = mat[l],[c]
                mc += 1
        ml += 1
return mat2