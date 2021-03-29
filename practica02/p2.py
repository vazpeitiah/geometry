import networkx as nx              # Importamos libreria para trabajar con grafos
import matplotlib.pyplot as plt    # Importamos libreria para dibujar con grafos
import numpy

#Funcion para colorear el grafo con el arreglo de colores colors
# Se usa un algoritmo voraz
def colorear_grafo(G, colors):

    for node in G.nodes():
        G.nodes[node]['color'] = 'white' # Color blanco por defecto (NO COLOREADO)

    # Se colorea el primer vértice con el primer color de la lista colors.
    G.nodes[0]['color'] = colors[0]
    print("se pinto el vertice 0 con " +colors[0])

    # Se usa un diccionario temporal para almacenar los colores disponibles. 
    # Falso cuando el color cr ya ha sido asignado a un verticie adyacente
    avaible = {}
    for c in colors:
        avaible[c] = True

    #Procedemos a colorear el resto de vertices
    for x in range(1, G.number_of_nodes()):
        for y in G[x]:# Recorremos la lista de vertices adyacentes al vertice x
            if (G.nodes[y].get('color') != 'white'): #Si el vertice se ha coloreado 
                avaible[G.nodes[y].get('color')] = False; # color no disponible
        
        #Encuentra el primer color disponible
        cr = 0
        for z in range(len(colors)):
            if(avaible[colors[z]]):
                cr = z
                break
        
        #Asigna el color cr al verice x
        G.nodes[x]['color'] = colors[cr]
        print("se pinto el vertice " + str(x) + " con " +colors[cr])

        #Volvemos a colocar a todos los colores disponibles para la siguiente iteracion
        for c in colors:
            avaible[c] = True

    #Obtenemos el color que se le asigno a cada nodo del grafo
    nodeColors = [G.nodes[node].get('color') for node in G.nodes()]

    # Dibujamos el grafo sin que se intersecten las aristas
    nx.draw_planar(G, with_labels = True, 
                      font_weight="bold", 
                      node_color = nodeColors) # Asigamos el color de los vertices
    plt.show() # Abrir visualizador de matplotlib

print("PRACTICA 02: ALGORITMO DE 3-COLORACION")
print("Introduce el nombre del archivo que contiene la matriz de adyacencia del grafo planar: ")
filename = str(input())

colors = []

print("Ingresa los colores: (máximo 3)")
for i in range(3):
    colors.append(str(input()))

with open(filename, 'r') as f:
    adjacency_matrix = numpy.matrix([[int(num) for num in line.split(' ')] for line in f])

G=nx.from_numpy_matrix(adjacency_matrix)

colorear_grafo(G, colors)