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


def list_routes(flights: List[Flight], start: Airport, b: Airport, t, T: timedelta) -> Optional[List[List[Flight]]]:
    current_path_duration = timedelta(0, 0)
    current_path = []
    paths = []

    available_flight_per_airport = dict()
    for flight in flights:
        if l(flight) >= t and a(flight)-l(flight) <= T:
            if s(flight) in available_flight_per_airport:
                available_flight_per_airport[s(flight)].append(flight)
            else:
                available_flight_per_airport[s(flight)] = [flight]

    find_possible_routes(available_flight_per_airport, start, b, t, T,current_path_duration, current_path, paths)
    return paths if len(paths) is not 0 else None


def find_possible_routes(flights: Dict, start: Airport, b: Airport, arrival_time: datetime, T: timedelta,
                         current_path_duration: timedelta, current_path: List, paths: List) -> None:
    if start == b:
        paths.append(current_path.copy())
    else:
        for flight in flights[start]:
            relative_cost = calc_weight(flight, s(flight), arrival_time)
            cost = current_path_duration + relative_cost
            if cost < T and arrival_time+c(start) <= l(flight):
                new_path_duration = current_path_duration + relative_cost
                new_path = current_path + [flight]
                find_possible_routes(flights, d(flight), b, a(flight), T, new_path_duration, new_path, paths)

def calc_weight(e: Flight, u: Airport, t: datetime) -> timedelta:
    duration = a(e) - l(e)
    waiting_for_flight = l(e) - (t + c(u))
    return duration + waiting_for_flight + c(u)
