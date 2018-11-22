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

    from ficher_avec_des_fonctions import *

On utilise la commande *from* et le signe *, pour dire :
« Dans le fichier "fichier_avec_des_fonctions" on importe tout. »
Vous l'aurez compris, on utilise ces parametres pour importer toute les fonctions qu'on aura crée dans le fichier.
