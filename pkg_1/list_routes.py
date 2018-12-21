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
    for src in airports:
        paths[src]=dict()
        for dest in airports:
            paths[src][dest] = dict()

    min_flight_duration = timedelta.max


    for flight in flights:
        if l(flight) >= t_start and a(flight)-l(flight) <= T:
            paths[s(flight)][d(flight)][a(flight) - l(flight)] = [1, [[flight]]]
            if a(flight) - l(flight) < min_flight_duration:
                min_flight_duration = a(flight) - l(flight) # volo più breve corrisponde al path più breve

    time_counting = min_flight_duration
    path_added = True
    while time_counting <= T and path_added:
        min_path_relative_duration = timedelta.max
        path_added = False
        for flight in flights:         # m
            for src in paths:          # n
                for possible_duration_time in paths[src][s(flight)]:
                    print("partenza volo ", l(flight))
                    print("durata del path ",possible_duration_time)
                    print("costo di check-in", c(s(flight)))
                    print("posso prenderlo? ", l(flight) >= t_start + possible_duration_time+c(s(flight)))
                    if l(flight) >= t_start + possible_duration_time+c(s(flight)):
                        path_duration = possible_duration_time
                        print("Quanto costa il volo? ")
                        flight_cost = calc_weight(flight, s(flight), t_start + path_duration)
                        print(flight_cost)
                        print("Posso ancora prenderlo rispetto alla durata di ",T)
                        path_relative_duration = path_duration + flight_cost
                        print("durata totale ", path_relative_duration," quindi ",path_relative_duration <= T)
                        if path_relative_duration <= T:
                            for path in paths[src][s(flight)][possible_duration_time][1]:
                                    new_path_discovered = path + [flight]

                                    print("Ho già considerato questo path? ")
                                    if path_relative_duration in paths[src][d(flight)] and new_path_discovered in paths[src][d(flight)][path_relative_duration][1]:
                                        print("SI")
                                    elif path_relative_duration in paths[src][d(flight)]:
                                        print("ADDING PATHS")
                                        path_added = True
                                        paths[src][d(flight)][path_relative_duration][1].append(new_path_discovered)
                                    else:
                                        print("ADDING PATHS")
                                        path_added = True
                                        paths[src][d(flight)][path_relative_duration] = [1, [new_path_discovered]]
                            print("path relative duration ",path_relative_duration)
                            if path_relative_duration < min_path_relative_duration:
                                print("UPDATE MIN")
                                min_path_relative_duration = path_relative_duration
        time_counting = min_path_relative_duration

        #print possible paths

    print("PATHS DURATION NUMBER IS  ",len(paths[start][end]))
    i = 1
    for time_valid in paths[start][end]:
        print(" PATH for time equal to ", time_valid)
        print("")
        print("PATH ", i)
        for flight_path in paths[start][end][time_valid][1]:
            print(flight_path)
        print("")
        i = i+1
        print("")


def calc_weight(e: Flight, u: Airport, t: datetime) -> timedelta:
    duration = a(e) - l(e)
    waiting_for_flight = l(e) - (t + c(u))
    return duration + waiting_for_flight + c(u)
