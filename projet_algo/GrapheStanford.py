import networkx as nx

import matplotlib.pyplot as plt
import numpy as np


def dessiner_graphe_facebook(nom_fichier):
    i = 0
    j = 0
    s = []
    r = []
    file = open(nom_fichier, 'r')
    data = file.read().splitlines()
    G = nx.Graph()
    for i in data:
        if len(i) >= 0:
            espace = i.split()
            # print(espace)
            s.append(int(espace[0]))
            r.append(int(espace[1]))
            G.add_edge(int(espace[0]), int(espace[1]))

    pos = nx.spring_layout(G)
    # fonction prédéfinie pour les noeuds du graphe
    nx.draw_networkx_nodes(G, pos, node_color="lavender", node_size=200)
    # fonction prédéfinie pour les étiquettes des nœuds sur le graphe G
    nx.draw_networkx_labels(G, pos)
    # fonction prédéfinie pour dessiner les aretes du graphe G
    nx.draw_networkx_edges(G, pos, arrows=False)
    # fonction prédéfinie pour écrire un titre dans le graphe G
    plt.title("la Génération d'un graphe aléatoire")

    return G
    plt.show()  # fonction prédéfinie pour afficher le graphe


def degre_max(graphe):
    liste_degree = sorted((d for n, d in graphe.degree()), reverse=True)
    dmax = max(liste_degree)
    print("Le degré maximum du graphe est : " + str(dmax))
    return(dmax)


"""
     fonction histogramme_graphe permettre de dessiner la valeur de plus haut degré du graphe

"""


def histogramme_graphe(graphe):
    # liste de qui retourne une liste de : (sommet, degre de sommet)
    degre_graphe = graphe.degree()
   # print(degre_graphe)
    # liste de qui filtre la liste de degre_graphe pour retourner la liste de degre
    liste_de_degre = sorted((d for n, d in degre_graphe), reverse=True)
    # print(liste_de_degre)

    fig = plt.figure("histogramme du graphe aléatoire ", figsize=(5, 5))
    axe = fig.add_subplot()
    # cette fontion nous permettre de créer les deux axes x ,y on fonction de degré et la nbre
    # des sommets ayant ce degré a partir de la liste_de_degre
    axe.bar(*np.unique(liste_de_degre, return_counts=True))
    axe.set_title("histogramme de degré -- nombre sommet")
    axe.set_xlabel("Degré")
    axe.set_ylabel("nombre des sommets ")
    fig.tight_layout()
    plt.show()


"""
        fonction nombre_chemein_longeur_2 permettre de trouver le nbre des chemins de longeur deux

 """


def nombre_chemein_longeur_2(graphe):
    #matrice = nx.adjacency_matrix(graphe)
    #matrice_adjacence_au_carrée = matrice*matrice
    matrice_adjacence = nx.to_numpy_matrix(graphe)
    #matrice_ad = np.matrix(matrice_adjacence)
    # print(matrice_ad)
    print("matrice d'adjacnece du graphe :")
    print(matrice_adjacence)
    matrice_adjacence_au_carrée = matrice_adjacence*matrice_adjacence
    print("matrice d'adjacnece au carre du graphe :")
    print(matrice_adjacence_au_carrée)
    diagonale_matrice = matrice_adjacence_au_carrée.diagonal()
    #diagonale = matrice_adjacence.diagonal()
    print("diagnole du matrice  :")
    print(diagonale_matrice)
    somme_matrice_carre = np.sum(matrice_adjacence_au_carrée)
    somme_diagonale_carre = np.sum(diagonale_matrice)
    """for i in range(nx.nodes(graphe).count):
        for j in range(sommet):
            if matrice_adjacence[i, j] == 1:
                somme_matrice_carre = somme_matrice_carre - \
                    matrice_adjacence_au_carrée[i, j]
    """
    #somme_matrice = np.sum(matrice_adjacence)

    #somme_diagonle_matrice = np.sum(diagonale)
    somme = ((somme_matrice_carre-somme_diagonale_carre)/2)
    print("nombre des chemins du longeur 2 est : "+str(somme))
