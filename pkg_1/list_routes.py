from typing import Optional, Dict
from airports_time_schedule.ATS import *

"""
    Progettare	una	 funzione	list_routes() che, preso	in	input l’orario	della	compagnia,
    gli	areoporti	a e	b,	 un	orario	 di	 partenza	t ed	 un	intervallo di	 tempo	T,	 restituisce	
    tutte	 le	 rotte che	 consentono	 di	 andare	 da	 a a	 b con	 un	 durata	 complessiva	 del	
    viaggio	 non	 superiore	 a	 T	 e	 con	 orario	 di	 partenza successivo a	 t.	 Una	 rotta	 è	
    costituita	da	una	sequenza	di	voli	e	la	sua	durata	è	data	dalla	somma	delle	durate	di	
    tutti	i	voli	più	i tempi	di	attesa	negli	scali per	le	coincidenze.	Ad	ogni	scalo	bisogna	
    considerare	 che	 non	 è	 possibile	 effettuare	 una	 coincidenza	 se	 tra	 l’orario	 di	
    atterraggio	di	un	volo	ed	il	tempo	di	decollo	del	volo	successivo	intercorre	un	tempo	
    inferiore a c(a).
    
"""

"""
def list_routes(airports: List[Airport], flights: List[Flight], start: Airport, end: Airport, t_start: datetime, T: timedelta) ->Optional[List[List[Flight]]]:
    # Table to be filled up using DP.
    # The value count[i][j][e] will / store
    # count of possible walks from i to
    # j in e minutes, the possible walks in a list of list of flights, for each walk the time remaining
    paths = dict()
    for src in airports:    # n*n
        paths[src]=dict()
        for dest in airports:
            paths[src][dest] = dict()

    for flight in flights:   # m
        if l(flight) >= t_start and a(flight)-l(flight) <= T:
            paths[s(flight)][d(flight)][a(flight) - l(flight)] = [[flight]]
    i=0
    path_added = True
    while path_added:  # T/flight_min *
        path_added = False
        for flight in flights:   # m *
            for src in paths:      # n *
                for possible_duration_time in paths[src][s(flight)]:  # T/flight_min *
                    if l(flight) >= t_start + possible_duration_time+c(s(flight)):
                        flight_cost = calc_weight(flight, s(flight), t_start + possible_duration_time)
                        path_relative_duration = possible_duration_time + flight_cost
                        if path_relative_duration <= T:
                            for path in paths[src][s(flight)][possible_duration_time]:  # boh *
                                    i+=1
                                    new_path_discovered = path + [flight]
                                    if path_relative_duration not in paths[src][d(flight)]:  # T/t_flight_min
                                        path_added = True
                                        paths[src][d(flight)][path_relative_duration] = [new_path_discovered]
                                    elif new_path_discovered not in paths[src][d(flight)][path_relative_duration]: # boh
                                        path_added = True
                                        paths[src][d(flight)][path_relative_duration].append(new_path_discovered)

    #print possible paths
    print("path visited ",i)
    routes = []
    for time_valid in paths[start][end]:
        for flight_path in paths[start][end][time_valid]:
            routes.append(flight_path)
    return None if len(routes) is 0 else routes
"""


def list_routes(flights: List[Flight], start: Airport, b: Airport, t, T: timedelta):
    current_path = [timedelta(0, 0), []]
    paths = []

    # Construction
    available_flight = dict()
    for flight in flights:
        if l(flight) >= t and a(flight)-l(flight) <= T:
            if s(flight) in available_flight:
                available_flight[s(flight)].append(flight)
            else:
                available_flight[s(flight)] = [flight]

    list_routes_rec(available_flight, start, b, t, T, current_path, paths)
    return paths


def list_routes_rec(flights: Dict, start: Airport, b: Airport, arrival_time: datetime, T: timedelta, current_path: List, paths: List):
    if start == b:
        paths.append(current_path[1].copy())
    else:
        for flight in flights[start]:
            actual_cost = calc_weight(flight, s(flight), arrival_time)
            cost = current_path[0] + actual_cost
            if cost < T and arrival_time+c(start) <= l(flight):
                current_path[0] += actual_cost
                current_path[1].append(flight)
                list_routes_rec(flights, d(flight), b, a(flight), T, current_path, paths)
                current_path[1].remove(flight)
                current_path[0] -= actual_cost


def calc_weight(e: Flight, u: Airport, t: datetime) -> timedelta:
    duration = a(e) - l(e)
    waiting_for_flight = l(e) - (t + c(u))
    return duration + waiting_for_flight + c(u)
