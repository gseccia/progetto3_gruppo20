from typing import Tuple, List, Optional
from TdP_collections.graphs.graph import Graph


"""
    Date le tre affermazioni (i) G e bipartito; (ii) ` G e 2-colorabile e (iii) ` G non contiene cicli di lunghezza
    dispari, dimostriamo (i) ⇒ (ii), (ii) ⇒ (iii), (iii) ⇒ (i). Questo dimostra che (i) ⇔ (ii) e (i) ⇔ (iii).
    
    1. Se G e bipartito, ` e 2-colorabile. Semplicemente, diamo colore ` 1 a tutti i nodi in una partizione, diamo
    colore 2 a tutti i nodi nell’altra. Non essendoci archi fra i nodi di una partizione, la colorazione e`
    valida.
    
    2. Se G e 2-colorabile, non contiene cicli di lunghezza dispari. Supponiamo per assurdo che esista un `
    ciclo (v1, v2),(v2, v3). . . ,(vk−1, vk),(vk, v1), con k dispari. Se il nodo v1 ha colore 1, il nodo v2
    deve avere colore 2; il nodo v3 deve avere colore 1, e cos`ı via fino al nodo vk, che deve avere colore 1.
    Poiche` v1 e successore di ` vk, v1 deve avere colore 2, assurdo.
    
    3. Se non esistono cicli di lunghezza dispari, il grafo e bipartito. Dimostriamo questa affermazione `
    costruttivamente. Si prenda un nodo x lo si assegna alla partizione S1. Si prendono poi tutti i nodi
    adiacenti a nodi in S1 e li si assegna alla partizione S2. Si prendono tutti i nodi adiacenti a nodi in S2
    e li si assegna alla partizione S1. Questo processo termina quando tutti i nodi appartengono ad una o
    all’altra partizione. Un nodo puo essere assegnato pi ` u di una volta se e solo se fa parte di un ciclo. Ma `
    affinche venga assegnato a due colori diversi, deve far parte di un ciclo di lunghezza dispari, e questo ´
    non e possibile.
"""


def bipartite(G: Graph) -> Optional[Tuple[List[Graph.Vertex], List[Graph.Vertex]]]:
    if G.is_directed():
        raise ValueError("Graph is supposed to be not directed. Directed graph given.")

    # Create a color array to store colors
    # assigned to all veritces. Vertex
    # number is used as index in this array.
    # The value '-1' of colorArr[i] is used to
    # indicate that no color is assigned to
    # vertex 'i'. The value 1 is used to indicate
    # first color is assigned and value 0
    # indicates second color is assigned.
    colorArr = {}
    for v in G.vertices():
        colorArr[v] = -1

    src = list(G.vertices())[0]

    # Assign first color to source
    colorArr[src] = 1

    # Create a queue (FIFO) of vertex numbers and
    # enqueue source vertex for BFS traversal
    queue = [src]
    first = []
    second = []
    # Run while there are vertices in queue
    # (Similar to BFS)
    while queue:

        u = queue.pop()

        for v in G.vertices():

            # An edge from u to v exists and destination
            # v is not colored
            if G.get_edge(u, v) is not None and colorArr[v] == -1:

                # Assign alternate color to this
                # adjacent v of u
                color = 1 - colorArr[u]
                colorArr[v] = color
                if color == 0:
                    first.append(v)
                elif color == 1:
                    second.append(v)
                queue.append(v)

            # An edge from u to v exists and destination
            # v is colored with same color as u
            elif G.get_edge(u, v) is not None and colorArr[v] == colorArr[u]:
                return None

    # If we reach here, then all adjacent
    # vertices can be colored with alternate
    # color
    return first, second


g = Graph()
v = []
for i in range(1, 9):
    v.append(g.insert_vertex(i))
g.insert_edge(v[0],v[1])
g.insert_edge(v[0],v[3])
g.insert_edge(v[2],v[1])
g.insert_edge(v[2],v[3])
g.insert_edge(v[2],v[5])
g.insert_edge(v[4],v[3])
g.insert_edge(v[4],v[5])
g.insert_edge(v[4],v[7])
g.insert_edge(v[6],v[5])
g.insert_edge(v[6],v[7])
#g.insert_edge(v[7],v[5])

X,Y = bipartite(g)
print("X partition")
for elem in X:
    print(elem)

print("Y partition")
for elem in Y:
    print(elem)