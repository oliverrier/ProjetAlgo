Module Det2(mat):

Explication Math:


    mat = [[a,b],[c,d]] 
    det(mat) = (a * d) - (c * b).


Algo:

    On vérifie tout d'abord que la matrice a bien une taille conforme pour notre fonction, c'est à dire qu'elle possède 2 lignes et 2 colonnes.
    On calcule ensuite la valeur de a * d puis la  valeur de c * b.
    On soustrait ensuite ces deux résultats et on obtient notre déterminant.

Module Reduit(mat,i,j):

Explication Maths:

    La réduction de matrice revient à faire passer une matrice 3x3 à une matrice 2x2.
    En effet en enlevant une ligne et une colonne à la matrice on obtient une matrice plus simple.
    On a besoin de matrice réduite pour le calcul du déterminant d'une matrice 3x3.

Algo:

    La fonction prend en paramètre la matrice 3x3, appellée mat, la ligne à enlever, ligne, et la colonne à enlever, colonne.
    On initialise tout d'abord une matrice 2x2, appelée mat2, avec toutes ses valeurs à 0 pour que ça soit plus simple à modifier.
    On initialise ensuite ml à 0, cette variable nous permettra de savoir quel valeur de notre mat2 nous allons modifier.
    On parcourt ensuite chaque ligne de notre matrice 3x3.
    On vérifie que la ligne que l'on parcourt actuellement est différente de la ligne que l'on veut enlever.
    On initialise ensuite mc qui à la même vocation que ml mais pour les colonne.
    Après ça on parcourt les colonnes de notre matrice 3x3.
    On vérifie que la colonne que l'on parcourt n'est pas celle que l'on veut enlever.
    et ensuite on récupère la valeur de la ligne et de la colonne que l'on parcourt actuellement pour la rentrer dans mat2 à la ligne ml et à la colonne mc.
    On incrémente ensuite mc à chaque fois qu'on parcourt une colonne valide et ml à chaque ligne valide.
    On renvoie ensuite notre matrice 2x2.


Module det2(mat):

Explication Maths:

    Le determinant d'une matrice 3x3 est plus compliqué à calculer qu'un déterminant de matrice 2x2.
    Pour une matrice 3x3 de la forme mat=[[a,b,c],[d,e,f],[g,h,i]]
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
    Le determinant d'une matrice 3x3 se calcule de la façon suivante :
    (a * determinant de la matrice 3x3 à la quelle on enlève la ligne 0 et la colonne 0) - (b * determinant de la matrice avec la linge 0 et la colonne 1 en moins + (c * determinant de la matrice sans la ligne 0 et la colonne 2).
    ou encore : 
    mat[0][0] * det2(reduit(mat,0,0)) - mat[0][1] * det2(reduit(mat,0,1)) + mat[0][2] * det2(reduit(mat,0,2))

Algo:

    On vérifie d'abord que la matrice est bien conforme et fait la bonne taille.
    Ensuite on utilise la fonction réduit(mat,ligne,colonne) et la fonction det2(mat) pour le calcul.
    On récupère ensuite mat[0][0] et le determinant de la matrice reduit(mat,0,0), puis mat[0][1] avec le determinant de la matrice reduit(mat,0,1) et enfin mat[0][2] avec le determinant de la matrice reduit(mat,0,2).
    On effectue ensuite le calcul de la façon suivante :
    mat[0][0]*det2(reduit(mat,0,0)) - mat[0][1]*det2(reduit(mat,0,1)) + mat[0][2]*det2(reduit(mat,0,2))


Module transposee(mat):

Explication Maths: 

    Pour avoir la transposée d'une matrice on doit intervertir ses lignes et ses colonnes.
    Pour une matrice 3x3 de type:
    [[a,b,c]
     [d,e,f]
     [g,h,i]]
    , sa transposee sera:
    [[a,d,g]
     [b,e,f]
     [c,f,i]]

Algorithme:

    Dans cette fonction on commence par initialiser une matrice 3x3,
    On parcourt chaque ligne et chaque colonne de la matrice donnée en paramètre puis on échange les indices lignes-colonnes par rapport à la matrice de base.
    On renvoie ensuite la matrice obtenue.

