from typing import Tuple, List, Optional
from TdP_collections.graphs.graph import Graph


"""
    Scrivere	una	funzione	bipartite() che,	preso	in	input	un	grafo	G	non	diretto,	verifica	
    se	 G	 è	 bipartito	 e	 restituisce	 una	 partizione	 (X,	 Y)	 dei	 vertici	 di	 G	 tale	 che	 tutti	 gli	
    archi	del	grafo	collegano	un	vertice	di	X	ad	un	vertice	di	Y. Nel	caso	in	cui	il	grafo	non	
    sia	 bipartito la	 funzione	 deve	 restituire	 None.	 Analizzare	 la	 complessità	 della	
    funzione	proposta.
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

    X = [src]  # partition with color 0
    Y = []  # partition with color 1

    # Run while there are vertices in queue
    # (Similar to BFS)
    while queue:

        u = queue.pop()

        for v in G.incident_edges(u):
            d = v.opposite(u)
            # An edge from u to v exists and destination
            # v is not colored
            if colorArr[d] == -1:

                # Assign alternate color to this
                # adjacent v of u
                color = 1 - colorArr[u]
                colorArr[d] = color
                if color == 1:
                    X.append(d)
                elif color == 0:
                    Y.append(d)
                queue.append(d)

            # An edge from u to v exists and destination
            # v is colored with same color as u
            elif colorArr[d] == colorArr[u]:
                return None

    # If we reach here, then all adjacent
    # vertices can be colored with alternate
    # color
    return X, Y
