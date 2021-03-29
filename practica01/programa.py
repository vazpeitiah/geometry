#!/usr/bin/python3

import networkx as nx              # Importamos libreria para trabajar con grafos
import matplotlib.pyplot as plt    # Importamos libreria para dibujar con grafos
import numpy

#Funcion para colorear un grafo con máximo 4 colores
# file --> archivo donde se encuentra la matriz de adyacencia del grafo
# colors --> arreglo de 4 colores
def colorear_grafo(G, colors):

    for node in G.nodes():
        G.nodes[node]['color'] = 'white' # Color blanco por defecto (NO COLOREADO)

    #Algoritmo principal
    i = 0
    for color in colors:
        if(i == G.number_of_nodes): #Si ya se pintaron todos los nodos terminar el algoritmo 
            break
        for node in G.nodes():
            if (G.nodes[node].get('color') == 'white'):
                flag = True
                for x in G[node]:
                    if (flag == False): #Si un vecino es del mismo color ya no se busca mas
                        break
                    if(G.nodes[x].get('color') == color):
                        flag = False
                if(flag):
                    #Si no se ha pintado aun el nodo y ninguno de sus 
                    #venciones es de color "color", entonces se pinta el nodo
                    G.nodes[node]['color'] = color
                    i += 1

    #Obtenemos el color que se le asigno a cada nodo del grafo
    nodeColors = [G.nodes[node].get('color') for node in G.nodes()] 

    nx.draw_planar(G, with_labels = True, 
                      font_weight="bold", 
                      node_color = nodeColors) # Dibujamos el grafo sin que se intersecten las aristas
    plt.show() # Abrir visualizador de matplotlib
    

print("introduce el nombre del archivo que contiene la matriz de adyacencia del grafo planar: ")
filename = str(input())

colors = []

print("Ingresa los colores: (máximo 4)")
for i in range(4):
    colors.append(str(input()))

with open(filename, 'r') as f:
    adjacency_matrix = numpy.matrix([[int(num) for num in line.split(' ')] for line in f])

G=nx.from_numpy_matrix(adjacency_matrix)

colorear_grafo(G, colors)