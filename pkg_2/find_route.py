from typing import Optional

from TdP_collections.list.positional_list import PositionalList
from airports_time_schedule.ATS import *
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


def find_route(flights: List[Flight], start: Airport, end: Airport, t_start: datetime) -> Optional[Tuple[timedelta, PositionalList]]:
    """
    La funzione	find_route() prende	in	input	l’orario	 della	 compagnia,
    gli	areoporti	a e	b,	ed	un	orario	di	partenza	t,	 e  trova	la	rotta	che	permette	di	arrivare
    da	a a	b nel	minor	tempo	possibile, partendo	ad	un	orario	non	precedente a	t.

    :param flights: lista di voli
    :param start: aeroporto di partenza
    :param end: aeroporto di destinazione
    :param t_start: orario di partenza
    :return: rotta	che	permette di	arrivare da	a a	b nel minor	tempo possibile o None se non trovato
    """

    dist = {}                           # Per ogni aereoporto, memorizzo il tempo per arrivarci
    cloud = {}                          # mappa contente la minor distanza per ogni aeroporto
    pq = AdaptableHeapPriorityQueue()   # ogni aeroporto viene memorizzato in una coda con priorità pari alla sua distanza
    pqlocator = {}                      # dizionario per accedere ad ogni elemento della coda

    t = {start: t_start}                # tempo in cui arrivo all'aereoporto x, inizialmente la sorgente con tempo di arrivo pari a t_start

    flights_used = {}                   # Dizionario che consente per ogni aereoporto di memorizzare il volo con cui ci sono arrivato

    # E' il percorso finale dei voli presi per andare da start a end
    path = PositionalList()

    # Creaiamo la matrice di incidenza dei voli in partenza da ogni aeroporto
    incident_flights = {}
    for flight in flights:
        if s(flight) not in incident_flights:
            incident_flights[s(flight)] = [flight]
        else:
            incident_flights[s(flight)].append(flight)

    dist[start] = timedelta(hours=0, minutes=0)                         # Inizialmemnte la distanza rispetto a start è 0
    pqlocator[start] = pq.add(dist[start], start)                       # memorizziamo la posizione di start all'interno della coda

                                                                        # itero finchè non ho più aeroporti da visitare
    while not pq.is_empty():
        key, u = pq.remove_min()                                        # prendo l'aeroporto in cui arrivo con meno tempo
        cloud[u] = key                                                  # aggiungo la distanza per u alla mappa delle distanze
        del pqlocator[u]                                                # rimuovo il locator per u

        if u == end:                                                    # se u è l'aeroporto di destinazione restituisco la soluzione
            path.add_first(flights_used[u])                             # il volo utilizzato per arrivare in u è aggiunto al path
            dep = s(flights_used[u])                                    # setto l'aeroporto corrente all'aeroporto di partenza
            while dep != start:                                         # finche non arrivo all'aeroporto di partenza
                path.add_first(flights_used[dep])                       # aggiungo il volo utilizzato per arrivare all'aeroporto corrente
                dep = s(flights_used[dep])                              # aggiorno l'aeroporto corrente
            return cloud[u], path                                       # ritorno la rotta e la sua durata

        for e in incident_flights[u]:                                   # per ogni volo in partenza da u
            if l(e) - t[u] >= c(u) or (u == start and l(e) >= t[u]):    # se il volo può essere considerato
                v = d(e)                                                # assegno a v l'aeroporto di arrivo
                if v not in dist:                                       # se non ho mai incontrato l'aeroporto
                    dist[v] = timedelta.max                             # pongo la distanza da start al massimo
                    pqlocator[v] = pq.add(dist[v], v)                   # aggiungo v agli aeroporti da considerare e ne memorizzo la posizione nella coda
                if v not in cloud:                                      # se non ho ancora aggiunto v alla soluzione
                    wgt = calc_weight(e, t)                             # calcolo il costo del volo corrente come tempo
                    if dist[u] + wgt < dist[v]:                         # il path che ho trovato è migliore di quello precedente?
                        dist[v] = dist[u] + wgt                         # aggiorno la distanza per arrivare all'aeroporto v
                        pq.update(pqlocator[v], dist[v], v)             # aggiorno il valore della distanza anche nella coda
                        t[v] = a(e)                                     # aggiorno il tempo di arrivo all'aeroporto v
                        flights_used[v] = e                             # segno il volo e come utilizzato per arrivare a v
    return None


def calc_weight(e: Flight, t: dict) -> timedelta:
    """
    :param e: volo corrente
    :param t: dizionario dei tempi di arrivo per ogni aeroporto
    :return: peso del volo in termini di durata della scelta
    """
    duration = a(e) - l(e)                              # durata del volo
    waiting_for_flight = l(e) - (t[s(e)] + c(s(e)))     # tempo di attesa
    return duration + waiting_for_flight + c(s(e))      # durata + tempo di attesa + tempo di coincidenza
