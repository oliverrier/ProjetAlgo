def transpose(mat):
    transpose=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,3):
        for j in range(0,3):
            transpose[j][i]=mat[i][j]
    return transpose
            
