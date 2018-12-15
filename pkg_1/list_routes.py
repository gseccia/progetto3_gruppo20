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


def list_routes_(airports: List[Airport], flights: List[Flight], start: Airport, end: Airport, t_start: datetime, T: timedelta) ->Optional[List[List[Flight]]]:
    # Table to be filled up using DP.
    # The value count[i][j][e] will / store
    # count of possible walks from i to
    # j in e minutes, the possible walks in a list of list of flights, for each walk the time remaining
    paths = dict()
    for src in airports:
        paths[src]=dict()
        for dest in airports:
            paths[src][dest] = dict()

    min_flight_duration = timedelta.max
    for flight in flights:
        if l(flight) >= t_start and a(flight)-l(flight) <= T:
            paths[s(flight)][d(flight)][a(flight) - l(flight)][0] = 1
            paths[s(flight)][d(flight)][a(flight) - l(flight)][1] = [flight]
            paths[s(flight)][d(flight)][a(flight) - l(flight)][2] = [a(flight) - l(flight)]
            if a(flight) - l(flight) < min_flight_duration:
                min_flight_duration = a(flight) - l(flight) # volo più breve corrisponde al path più breve

    time_counting = min_flight_duration
    path_added = True
    while time_counting <= T and path_added:
        min_path_relative_duration = T
        path_added = False
        for flight in flights:
            for src in paths:
                num_existing_paths = paths[src][s(flight)][time_counting][0]
                if num_existing_paths != 0:
                    path = paths[src][s(flight)][time_counting][1][num_existing_paths-1]
                    path_duration = paths[src][s(flight)][time_counting][2][num_existing_paths-1]
                    flight_cost = calc_weight(flight, s(flight), t_start+path_duration)
                    path_relative_duration = path_duration+flight_cost
                    if path_relative_duration <= T:
                        new_path_discovered = path.append(flight)
                        path_added = True
                        if path_relative_duration in paths[src][d(flight)]:
                            paths[src][d(flight)][path_relative_duration][0] += 1
                            paths[src][d(flight)][path_relative_duration][1].append(new_path_discovered)
                            paths[src][d(flight)][path_relative_duration][2].append(path_relative_duration)
                        else:
                            paths[src][d(flight)][path_relative_duration][0] = 1
                            paths[src][d(flight)][path_relative_duration][1] = [new_path_discovered]
                            paths[src][d(flight)][path_relative_duration][2] = [path_relative_duration]

                    if path_relative_duration < min_path_relative_duration:
                        min_path_relative_duration = path_relative_duration
        time_counting = time_counting+min_path_relative_duration

        #print possible paths
        for time_valid in paths[start][end]:
            for path_series in paths[start][end][time_valid][1]:
                for path in path_series:
                    print(path)


def calc_weight(e: Flight, u: Airport, t: datetime) -> timedelta:
    duration = a(e) - l(e)
    waiting_for_flight = l(e) - (t + c(u))
    return duration + waiting_for_flight + c(u)
