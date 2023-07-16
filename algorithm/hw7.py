class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []   #Edges in Adjacency List

def initial_graph(n:int, edge_list:list)->list:
    graph = []
    for i in range(n):
        graph.append(GraphVertex(i))
    for e in edge_list:
        if 0 <= e[0] < n and 0 <= e[1] < n:
            graph[e[0]].edges.append(graph[e[1]])
    return graph
"""
We can represent a graph G as an adjacency matrix which is using an n*n matrix M, where element M[i][j] = 1 if (i, j) is an edge of G, and 0 if it isn’t.

Write a method in python as following :

def to_adj_matrix(graph:list)->list:
To convert a graph from adjacency list which is a list of GraphVertex class to adjacency matrix in type of nested list of int.

The GraphVertex class and supporting method initial_graph are included and declared as:

"""
def to_adj_matrix(graph:list)->list:
    M = [x[:] for x in [[0]*len(graph)]*len(graph)]
    for i in range(len(graph)):
        for j in range(len(graph[i].edges)):
            M[i][graph[i].edges[j].label] =1 
    return M





print(to_adj_matrix(initial_graph(5, [[2, 4], [4, 2], [1, 4], [4, 1], [3, 4], [4, 3], [1, 3], [3, 1]])))


"""
Consider a collection of electrical pins on a printed circuit board (PCB). For each pair of pins, there may or may not be a wire joining them.
We want to divide the pins on PCB to two parts. The same part of pins should not be connected, all wires must connect between parts.

Write a method in python as following :

def is_circuit_wireable(pcb:list)->bool:
To design an algorithm that takes a set of pins and a set of wires connecting pairs of pins representing as an adjacency list of Pin class pcb, and determines if it is possible to place some pins on the left half of a PCB, and the remainder on the right half, such that each wire is between left and right halves.
Return True, if such a division exists.

The Pin class and supporting method initial_pcb are included and declared as:

"""
class Pin:
    def __init__(self):
        self.side = -1
        self.wires = []

def initial_pcb(n:int, wire_list:list)->list:
    pcb = []
    for i in range(n):
        pcb.append(Pin())
    for w in wire_list:
        if 0 <= w[0] < n and 0 <= w[1] < n:
            pcb[w[0]].wires.append(pcb[w[1]])
    return pcb

def is_circuit_wireable(pcb:list)->bool:
