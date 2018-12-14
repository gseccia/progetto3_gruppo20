from datetime import datetime, timedelta
from typing import Optional
from airports_time_schedule.ATS import *
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


"""
    Progettare	 una	 funzione	find_route() che,	 preso	in	input	l’orario	 della	 compagnia,	
    gli	areoporti	a e	b,	ed	un	orario	di	partenza	t,	trova	la	rotta	che	permette	di	arrivare	
    da	a a	b nel	minor	tempo	possibile, partendo	ad	un	orario	non	precedente a	t.	(Come	
    per	l’esercizio	precedente,	bisogna	tener	conto	del	tempo	minimo	di	coincidenza	di	
    ogni	scalo).	
"""


def find_route(flights: List[Flight], start: Airport, end: Airport, t_start: datetime) -> Optional[Tuple[timedelta,List[Flight]]]:
    dist = {}  # d[v] is upper bound from s to v
    cloud = {}  # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()  # vertex v will have key d[v]
    pqlocator = {}  # map from vertex to its pq locator
    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance

    t = {start:  t_start + c(start)}

    flights_used = {}
    path = []

    incident_flights = {}
    for flight in flights:
        if s(flight) not in incident_flights:
            incident_flights[s(flight)] = [flight]
        else:
            incident_flights[s(flight)].append(flight)
    print(incident_flights)

    dist[start] = c(start)
    pqlocator[start] = pq.add(dist[start], start)  # save locator for future updates

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key  # its correct d[u] value
        del pqlocator[u]  # u is no longer in pq
        print("u ",u," cloud[u] ",cloud[u])
        if u == end:
            dep= s(flights_used[u])
            path.append(flights_used[u])
            while dep != start:
                print("DEP 1 ",dep)
                path.append(flights_used[dep])
                dep=s(flights_used[dep])
                print("DEP 2 ",dep)
            path.reverse()
            return cloud[u],path
        for e in incident_flights[u]:  # outgoing edges (u,v)
            v = d(e)
            if v not in dist:
                dist[v] = timedelta.max
                pqlocator[v] = pq.add(dist[v], v)
            if (l(e) - t[u] - c(u)).total_seconds() >= 0:
                if v not in cloud:
                    # perform relaxation step on edge (u,v)
                    wgt = calc_weight(e, u, t)  # COST FUNCTION
                    if dist[u] + wgt < dist[v]:  # better path to v?
                        dist[v] = dist[u] + wgt  # update the distance
                        pq.update(pqlocator[v], dist[v], v)  # update the pq entry
                        t[v] = t[u] + wgt
                        print("v ", v)
                        print("t[v] ",t[v])
                        print("dist[v] ",dist[v])
                        flights_used[v] = e

    return None


def calc_weight(e: Flight, u: Airport, t: dict) -> timedelta:
    duration = a(e) - l(e)
    print("duration ",duration)
    waiting_for_flight = l(e) - (t[u]+c(u))
    print("waiting ",waiting_for_flight)
    return duration + waiting_for_flight + c(u)
