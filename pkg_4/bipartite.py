from typing import Tuple, Set, List, Optional
from TdP_collections.graphs.graph import Graph

"""
    Scrivere	una	funzione	bipartite() che,	preso	in	input	un	grafo	G	non	diretto,	verifica	
    se	 G	 è	 bipartito	 e	 restituisce	 una	 partizione	 (X,	 Y)	 dei	 vertici	 di	 G	 tale	 che	 tutti	 gli	
    archi	del	grafo	collegano	un	vertice	di	X	ad	un	vertice	di	Y. Nel	caso	in	cui	il	grafo	non	
    sia	 bipartito la	 funzione	 deve	 restituire	 None.	 Analizzare	 la	 complessità	 della	
    funzione	proposta.
"""


def bipartite(g: Graph) -> Optional[Tuple[List[Graph.Vertex], List[Graph.Vertex]]]:
    visited = set()  # Insieme dei vertici visitati
    x = []           # init partizione 1
    y = []           # init partizione 2
    for u in g.vertices():  # per ogni vertice del grafo
        if u not in visited:  # che non ho ancora visitato
            visited.add(u)  # lo segno come visitato
            result = bipartite_connected(g, u, visited)  # calcolo bipartite della componente connessa del grafo
                                                         # in cui si trova il vertice
            if result is not None:   # se la componente connessa è bipartibile
                x = x + result[0]    # aggiorno la partizione 1
                y = y + result[1]    # aggiorno la partizione 2
            else:   # altrimenti
                return None          # il grafo non è bipartibile
    return x, y                      # restituisco le partizioni


def bipartite_connected(g: Graph, s: Graph.Vertex, discovered: Set[Graph.Vertex]) -> Optional[Tuple[List[Graph.Vertex], List[Graph.Vertex]]]:
    colour = {s: 0}  # assegno al primo vertice colore 0
    q = [s]          # creo una coda con i vertici da considerare
    x = [s]          # creo la sotto-partizione 1 con assegnato il primo vertice
    y = []           # creo la sotto- partizione 2
    while q:
        current = q.pop()  # prendo il vertice da elaborare
        next_colour = 1 - colour[current]  # i vertici opposti avranno colore opposto al vertice corrente
        for dest in g.incident_edges(current):  # considero tutti gli archi uscenti
            v = dest.opposite(current)   # e mi prendo il vertice opposto
            if v not in discovered:    # se è la prima volta che vedo quel vertice
                discovered.add(v)      # lo segno come visitato
                colour[v] = next_colour   # gli assegno il nuovo colore
                if next_colour == 0:    # se 0
                    x.append(v)    # lo assegno alla prima sotto-partizione
                else:    # altrimenti
                    y.append(v)   # lo assegno alla seconda sotto-partizione
                q.append(v)  # il vertice visitato dovrà essere considerato al prossimo ciclo
            elif colour[v] != next_colour:  # altrimenti se ho già visto il vertice e il suo colore non è opposto al vertice corrente
                return None   # la componente connessa al vertice sorgente non è bipartibile
    return x, y  # se arrivo qui vuol dire che è bipartibile e restituisco le partizioni
