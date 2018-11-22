TEST de det2:


    import libmatrice as l

    mat = [[4, 6], [9, 3]]

    print(l.det2(mat))

    Résultat: -42

    

    En effet pour calculer def 2 il faut faire 4*3-6*9 = 12 - 54 et le résultat est bien -42.




Test de transpose:


    import libmatrice as l

    mat = [[4, 6, 2], [9, 3, 5], [8, 1, 7]]

    print(l.transpose(mat))

    Résultat : [[4, 9, 8], [6, 3, 1], [2, 5, 7]]



    _En effet pour calculer transpose il faut inverser les ligne et colonne donc cela donne bien [[4, 9, 8], [6, 3, 1], [2, 5, 7]]_




TEST de reduit:


    import libmatrice as l

    mat = [[4, 6, 2], [9, 3, 5], [8, 1, 7]]

    print(l.reduit(mat, 0, 0))

    Résultat: [[3, 5], [1, 7]]



    _En effet pour calculer reduit il faut supprimer une ligne et une colonne et donc dans ce cas là cela donne cela donne bien [[3, 5], [1, 7]]_





TEST de det3:


    import libmatrice as l

    mat = [[4, 6, 2], [9, 3, 5], [8, 1, 7]]

    print(l.det3(mat))

    Résultat: -104



    _En effet pour calculer def 3 il faut faire 4 * reduit (mat, 0, 0) - 6 * reduit(mat, 0, 1) + 2 * reduit(mat, 0, 2) et le résultat est bien -104_




TEST de comatrice:


    import libmatrice as l

    mat = [[4, 6, 2], [9, 3, 5], [8, 1, 7]]

    print(l.comatrice(mat))

    Résultat: [[16, -23, -15], [-40, 12, 44], [24, -2, -42]]



    _En effet pour calculer comatrice il faut calculer (-1)^(i+j) pour savoir si c'est positif et multiplier par det2(reduit(mat,i,j)) et cela donne cela donne bien [[16, -23, -15], [-40, 12, 44], [24, -2, -42]]_


TEST inverse:


    import libmatrice as l

    mat = [[4, 6, 2], [9, 3, 5], [8, 1, 7]]

    print(l.inverse(mat))

    Résultat (affiché en nombre décimal) : [[-0.15384615384615385, 0.38461538461538464, -0.23076923076923078], [0.22115384615384615, -0.11538461538461539, 0.019230769230769232], [0.14423076923076922, -0.4230769230769231, 0.40384615384615385]] 



    _En effet pour calculer inverse il faut diviser la transposé de la comatrice de cette matrice par le déterminant de cette matrice. La transposé de cette comatrice est [[16, -40, 24], [-23, 12, -2], [-15, 44, -42]] et ce résultat divisé par -104 qui est le déterminant de la matrice donne bien le même résultat._
