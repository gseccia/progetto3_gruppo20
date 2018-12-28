from typing import Optional, Dict
from airports_time_schedule.ATS import *


def list_routes(flights: List[Flight], start: Airport, b: Airport, t: datetime, T: timedelta) -> Optional[
    List[List[Flight]]]:
    """
    La funzione	list_routes() prende in	input l’orario	della	compagnia,
    gli	areoporti	a e	b,	 un	orario	 di	 partenza	t ed	 un	intervallo di	 tempo	T e	 restituisce	
    tutte	 le	 rotte che	 consentono	 di	 andare	 da	 a a	 b con	 un	 durata	 complessiva	 del	
    viaggio	 non	 superiore	 a	 T	 e	 con	 orario	 di	 partenza successivo a	 t.
    
    :param flights: lista voli
    :param start: aeroporto di partenza
    :param b: aeroporto di destinazione
    :param t: tempo di partenza
    :param T: durata massima della rotta
    :return: rotte possibili o None se non presenti
    """
    current_path_duration = timedelta(0, 0)  # Inizializziamo la durata della possibile soluzione corrente a 0
    current_path = []  # Inizializziamo la possibile soluzione corrente
    paths = []  # Inizializziamo il container di tuttle le possibili soluzioni

    # Creaiamo la matrice di incidenza dei voli in partenza da ogni aeroporto
    available_flight_per_airport = dict()
    for flight in flights:
        if l(flight) >= t and a(flight) - l(flight) <= T:
            if s(flight) in available_flight_per_airport:
                available_flight_per_airport[s(flight)].append(flight)
            else:
                available_flight_per_airport[s(flight)] = [flight]

    # Chiamata alla funzione ricorsiva per la ricerca delle possibili soluzioni
    find_possible_routes(available_flight_per_airport, start, b, t, T, current_path_duration, current_path, paths)

    # Ritorna le possibili rotte altrimenti None
    return paths if len(paths) is not 0 else None


def find_possible_routes(flights: Dict, start: Airport, b: Airport, arrival_time: datetime, T: timedelta,
                         current_path_duration: timedelta, current_path: List, paths: List) -> None:
    """
    Il metodo find_possible_routes, dati i parametri di ingresso, aggiungerà a paths le rotte valide.

    :param flights: dizionario di voli in partenza da ogni aeroporto
    :param start: aeroporto di partenza
    :param b: aeroporto di destinazione
    :param arrival_time: orario di partenza dall'aeroporto start
    :param T: durata massima della rotta
    :param current_path_duration: durata della rotta corrente
    :param current_path: rotta corrente
    :param paths: lista soluzioni (conterrà il risultato della ricerca)
    :return: None
    """

    # Caso Base: rotta valida
    if start == b:
        paths.append(current_path.copy())  # aggiungo la rotta corrente a paths
    else:
        for flight in flights[start]:  # per ogni volo in partenza da start
            relative_cost = calc_weight(flight, arrival_time)  # calcolo il costo del volo corrente come tempo
            cost = current_path_duration + relative_cost  # calcolo il costo della rotta data l'aggiunta del volo
            if cost < T and arrival_time + c(start) <= l(
                    flight):  # verifico che il volo corrente permette l'esplorazione di nuove rotte
                new_path = current_path + [flight]  # creo una nuova possibile rotta
                find_possible_routes(flights, d(flight), b, a(flight), T, cost, new_path,
                                     paths)  # cerco le soluzioni a partire dalla nuova rotta


def calc_weight(e: Flight, t: datetime) -> timedelta:
    """
    :param e: volo corrente
    :param t: orario di partenza
    :return: peso del volo in termini di durata della scelta
    """
    duration = a(e) - l(e)  # durata del volo
    waiting_for_flight = l(e) - (t + c(s(e)))  # tempo di attesa
    return duration + waiting_for_flight + c(s(e))  # durata + tempo di attesa + tempo di coincidenza
