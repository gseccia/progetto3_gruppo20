from typing import Optional
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


def calc_weight(e: Flight, u: Airport, t: datetime) -> timedelta:
    duration = a(e) - l(e)
    waiting_for_flight = l(e) - (t + c(u))
    return duration + waiting_for_flight + c(u)
