from datetime import timedelta
from typing import Optional
from airports_time_schedule.ATS_graph import *
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


"""
    Progettare	 una	 funzione	find_route() che,	 preso	in	input	l’orario	 della	 compagnia,	
    gli	areoporti	a e	b,	ed	un	orario	di	partenza	t,	trova	la	rotta	che	permette	di	arrivare	
    da	a a	b nel	minor	tempo	possibile, partendo	ad	un	orario	non	precedente a	t.	(Come	
    per	l’esercizio	precedente,	bisogna	tener	conto	del	tempo	minimo	di	coincidenza	di	
    ogni	scalo).	
"""


def find_route(G: ATS, start: ATS.Airport, end: ATS.Airport, t: time) -> Optional[List[ATS.Flight]]:
    dist = {}  # d[v] is upper bound from s to v
    cloud = {}  # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()  # vertex v will have key d[v]
    pqlocator = {}  # map from vertex to its pq locator
    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in G.vertices():
        if v is start:
            dist[v] = c(v)
        else:
            dist[v] = float('inf')  # syntax for positive infinity
        pqlocator[v] = pq.add(dist[v], v)  # save locator for future updates

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key  # its correct d[u] value
        del pqlocator[u]  # u is no longer in pq
        for e in g.incident_edges(u):  # outgoing edges (u,v)
            v = e.opposite(u)
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                wgt = timedelta(l(e).hour - a(e).hour, l(e).min - a(e).min).total_seconds()/60 + c(v)     # COST FUNCTION UPDATED
                if dist[u] + wgt < dist[v]:  # better path to v?
                    dist[v] = dist[u] + wgt  # update the distance
                    pq.update(pqlocator[v], dist[v], v)  # update the pq entry
                    if v == end:
                        break
    return None
