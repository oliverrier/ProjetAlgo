def det3(mat):
    #Condition taille 
    if len(mat)!=3 or len(mat[0])!=3 or len(mat[1])!=3 or len(mat[2])!=3:
        return 'error'
    determ3=mat[0][0]*reduit(mat,0,0)-mat[0][1]*reduit(mat,0,1)+mat[0][2]*reduit(mat,0,2)
