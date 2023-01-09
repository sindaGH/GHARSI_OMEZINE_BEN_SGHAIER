import time
from matplotlib import pyplot as plt
from Graphe import Graphe
import networkx as nx
if __name__ == '__main__':
    """
    Partie 1 : 1- generation graphe aléatoire
                    maximum degre
                    histogramme sommet degre
                    nombre des chemins du longeur 2
                2- implementation base de donnée Stanfold
    """
    # on initialise un graphe de le nombre des sommets donnée en paramètre
    print("--------------------Partie 1---------------------------------")
    G = Graphe(15)
    G.generer_graphe()
    print("Dictionnaire du graphe : La liste d'adjacence du graphe")
    print(G.dictionnaire)
    g = G.dessiner_graphe_aleatoire()
    degreMax = G.afficher_degre_max(graphe=g)
    print("Le degré maximum du graphe est : "+str(degreMax))
    G.histogramme_graphe(graphe=g)
    nbreChemins = G.nombre_chemins_longeur(graphe=g)
    print("Le nombre des chemins du longeur 2 du graphe est :"+str(nbreChemins))
    """
    Cette partie de code pour tester les grands bases de Scantfold elle prend en paramètre le nom_du_fichier.txt
    g = dessiner_graphe_facebook(".facebook_combined.txt")
        histogramme_graphe(g)
        degre_max(g)
        plt.show()

    """
    """
    Partie 2 : implémentation algo du bron kerbosch version avec pivot
    """
    print("--------------------Partie 2---------------------------------")
    P = nx.nodes(G=g)
    r = []
    x = []
    # liste des cliques maximales du graphe retourner par l'algo de bron_kerbosch
    listCliques = G.bron_kerbosch_avec_pivot(graphe=g, P=P, R=None, X=None)
    print("les cliques maximales dans ce graphes sont :  ")
    for element in listCliques:
        print(element)
    print("--------------------Partie 3---------------------------------")
    L = G.degenerecy(g)
    print("La liste du degenerescence du graphe est  : ")
    print(L)
   # operator_ss_graphes = G.generer_sous_graphes(listeDegenerescence=L)
   # print("Les sous graphes Gi  générés  sont :")
    # for ss_graphe in operator_ss_graphes:
    #   print(ss_graphe)
    plt.show()
