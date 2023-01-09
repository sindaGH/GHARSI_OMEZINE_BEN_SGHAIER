"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%               Outils Pour La Conception D'Algorithmes
%   Auteurs: Gharsi Sinda
             Omezzine Manar
             Ben Sghaier Mohammed Ameur
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        première partie: 1- generation graphe aléatoire 
                            maximum degre
                            histogramme sommet degre 
                            nombre des chemins du longeur 2
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                    
"""

dictionnaire = {}


class Graphe:
    def __init__(self, sommet):
        # variable sommet pour initialiser nombre des sommets
        self.sommet = sommet
        # dictionnaire pour manipuler le graphe
        # clé : sommet , valeurs : liste des voisins du sommet
        self.dictionnaire = dictionnaire
    """
     fonction generer_graphe permettre à gérer le graphe aléatoirement selon la probabilité p
    """

    def generer_graphe(self):
        i = 0
        j = 0
        for i in range(self.sommet):
            self.dictionnaire[i] = list()
            for j in range(self.sommet):
                # proba p pour choisir si on ajoute le sommet j à la liste des voisins de i ou non
                proba = random.gauss(0, 2)
                if (proba > 0) and (proba < 1):
                    if (int(i) != int(j)):
                        self.dictionnaire[i].append(str(j))
    """
     fonction dessiner_graphe permettre de dessiner le graphe selon les valeurs de
     son dictionnaire correspondant en utlisant les fonctions prédéfini de la bibliothèque networkX

    """

    def dessiner_graphe_aleatoire(self):
        G = nx.Graph()
        for keys in self.dictionnaire.keys():
            G.add_node(int(keys))

        for keys, valuues in self.dictionnaire.items():
            for value in valuues:
                G.add_edge(int(keys), int(value))

        pos = nx.spring_layout(G)
        # fonction prédéfinie pour les noeuds du graphe
        nx.draw_networkx_nodes(G, pos, node_color="lavender", node_size=800)
        # fonction prédéfinie pour dessiner les aretes du graphe G
        nx.draw_networkx_edges(G, pos, arrows=False)
        # fonction prédéfinie pour les étiquettes des nœuds sur le graphe G
        nx.draw_networkx_labels(G, pos)
       # fonction prédéfinie pour écrire un titre dans le graphe G
        plt.title("la Génération d'un graphe aléatoire")
        return G
    """
     fonction  afficher_degre_max  permettre de retourner  la valeur de plus haut degré du graphe

    """

    def afficher_degre_max(self, graphe):
        liste_degree = sorted((d for n, d in graphe.degree()), reverse=True)
        dmax = max(liste_degree)
       # print("Le degré maximum du graphe est : " + str(dmax))
        return(dmax)
    """
     fonction histogramme_graphe permettre de dessiner la valeur de plus haut degré du graphe

    """

    def histogramme_graphe(self, graphe):
        '''

        '''
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
        # plt.show()
    """
     fonction nombre_chemein_longeur_2 permettre de trouver le nbre des chemins de longeur deux

    """

    def nombre_chemins_longeur(self, graphe):
        # on prend le matrice d'adjacence générer à partir le graphe
        # le matrice est symétrique puisque le graphe n'est pas orienté
        matrice_adjacence = nx.to_numpy_matrix(graphe)
        # on calule le matrice au carrée pour qu'on peut determiner les chemins du longeur 2
        matrice_adjacence_au_carrée = matrice_adjacence*matrice_adjacence
        diagonale_matrice = matrice_adjacence_au_carrée.diagonal()
        # somme des valeurs du matrice d'adjacence au carrée
        somme_matrice_carre = np.sum(matrice_adjacence_au_carrée)
        # somme des valeurs du diagnale de matrice d'adjacence
        somme_diagonale_carre = np.sum(diagonale_matrice)
        # cette boucle pour ne pas compter le nombre de chemins ayant une arrete entre
        # les deux sommets on  soustraire les valeurs de la somme du matrice d'adjacence
        for i in range(int((self.sommet))):
            for j in range(self.sommet):
                if matrice_adjacence[i, j] == 1:
                    somme_matrice_carre = somme_matrice_carre - \
                        matrice_adjacence_au_carrée[i, j]
        # somme est la somme globale on calcule la somme des valeurs du matrice / 2
        somme = ((somme_matrice_carre-somme_diagonale_carre
                  )/2)
       # print("nombre des chemins du longeur 2 est : "+str(somme))
        return (somme)

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        deuxième  partie  : implémentation d'algo bron_kerbosch_avec_pivot
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """

    def bron_kerbosch_avec_pivot(self, graphe,  P, R, X):

        P = list(P)
        R = list() if R is None else R
        X = list() if X is None else X

        if len(P + X) == 0:
            yield R
        else:
            # choisir un pivot on utilisant l'algo de Tomita
            pivot = self.pivot_tomita(graphe, P, X)
            for sommet in list(set(P).difference(nx.neighbors(graphe, pivot))):
                yield from self.bron_kerbosch_avec_pivot(graphe, list(set(P) & set(nx.neighbors(graphe, sommet))), R + [sommet],
                                                         list(set(X) & set(nx.neighbors(graphe, sommet))))

                P.remove(sommet)
                X.append(sommet)

    def pivot_tomita(self, graphe, P, X):

        P_union_X = list(P + X)
        # on prend le premier element u de P union X
        u = P_union_X[0]
        # L'intersection de P et les voisins de u
        P_inter_voisin_de_u = list(set(P) & set(nx.neighbors(graphe, u)))

        # on initialise le degre max à la taille de la liste  P inter voisins u
        degre_max = len(P_inter_voisin_de_u)
        # P union X \ {u}
        P_union_X_privee_de_sommet = list(set(P_union_X) - {0})
        # On cherche l'elment ayant le degre_max ds la liste P union X \ {u}
        for v in P_union_X_privee_de_sommet:

            P_inter_voisin_de_v = list(set(P) & set(nx.neighbors(graphe, v)))
            if len(P_inter_voisin_de_v) > degre_max:
                u = v
                degre_max = len(P_inter_voisin_de_v)
        return u

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    troisième  partie  : implémentation des algorithmes liés à l'énumération
                des cliques et de bicliques maximales
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """

    def degenerecy(self, graphe):
        # liste de degenerescence
        ListeDeg = []
        # liste D initialisé dans chaque case d'un indice les sommets ayant ce degré i
        D = []
        degreMax = self.afficher_degre_max(graphe=graphe)
        D = [list() for i in range(degreMax + 1)]
        for node in nx.nodes(graphe):
            i = graphe.degree(node)
            D[i].append(node)
       # print("Liste degre-sommet : ")
      #  print(D)
        x = 0
        while x <= self.sommet:
            for i in range(degreMax + 1):
                j = 0
                # si D[i]=0 rien à faire
                if len(D[i]) >= 1:
                    # si la case i avait plusqu'un sommet de degré i on parcours tous les sommets d'un de degré i
                    while j < len(D[i]):
                        sommet = random.choice(D[i])
                        ListeDeg.append(sommet)
                        D[i].remove(sommet)
                        neighborsSommet = graphe.neighbors(sommet)
                        # on parcours tous les sommets voisins du le sommet courant
                        # pour soustraire -1 de leur degre : les decaler à la case i-1
                        for neighbor in neighborsSommet:
                            if neighbor not in ListeDeg:
                                iterateur = filter(
                                    lambda x: x not in ListeDeg or x == sommet, graphe.neighbors(neighbor))
                                degreNeighbor = len(list(iterateur))
                                if degreNeighbor > 0:
                                    if neighbor in D[degreNeighbor]:
                                        D[degreNeighbor].remove(neighbor)
                                        D[degreNeighbor -
                                            1].append(int(neighbor))
                    j = j+1
            x = x + 1
        return ListeDeg

# Cette fonction permet de générer récursivement tous les sous-graphes d'un graphe
    def generer_sous_graphes(self, graphe,  listeDegenerescence):
        liste_graphe = []
        liste_nodes = nx.nodes(graphe)
        liste_arete = nx.edges(graphe)
        liste_sommet_2 = []
        for node in liste_nodes:
            for neighbor in graphe.neighbors(node):
                for neighbor_dis_2 in neighbor:
                    liste_sommet_2.append(neighbor_dis_2)
        for nodes in liste_nodes:
            graphe_tmp = Graphe()
            vi = {nodes}
            ni = {}

        return liste_graphe
