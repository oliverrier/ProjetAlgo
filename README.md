# Librairie python: libmatrice
>## *Qu'est-ce qu'une librairie ?*

Une **librairie** est un ensemble de **modules** (aussi appelés **fonctions**) qui peuvent être utiliser dans plusieurs programmes.
Cela évite d'écrire tout le temps la même chose dans plusieurs programme.

*Ah je vois, c'est beaucoup plus pratique !*
>## *Mais qu'est-ce qu'une fonction ?*
Une fonction est un morceau de programme qui permet de **réaliser plusieurs taches** et qui prend en compte des **parametres**.

Pour créer une fonction nous allons utiliser la fonction *def* :

    def ma_fonction(parametre):
        *fait quelque chose*
        return resultat

*Je comprends mieux. Mais si je peux l'utiliser dans plusieurs programmes...*
>## *Comment je l'ajoute dans d'autres programmes ?*

C'est très simple il suffit de l'appelé avec la commande *import* :

    from ficher_contenant import *

On utilise la commande *from* et le signe *, pour dire :
« Dans le fichier "fichier_contenant" on importe tout. »
Vous l'aurez compris, on utilise *from* pour dire que on chercher dans le fichier et le signe * signifie simplement tout.

*Ah oui je vois, donc si libmatrice est une librairie...*

>## Que fait la librairie libmatrice ?

La librairie libmatrice contient toutes les fonctions qui permettent d'inverser une matrice 3x3.

>## Comment on inverse une matrice ?

L'inversion de la matrice c'est la transposé de la matrice divisé par 