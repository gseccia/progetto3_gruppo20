from typing import Optional
from airports_time_schedule.ATS import *

"""
    Un	 volo	 consuma	 60kg	 di	 gasolio	 per	 ogni	 ora	 di	 volo	 e	 prima	 del	 decollo	 la	
    compagnia	 deve	 acquistare	 dal	 gesture dell’areoporto	 il	 gasolio	 necessario	 per	 il	
    volo.	Si	assuma che	ogni	kg	di	gasolio	costa	1€ e	che	la compagnia	ha	a	disposizione	
    un	 budget	 complessivo	 uguale	 a	 B	 per	 pagare	 il	 gasolio	 e	 che	 questo	 budget non	
    consente	 di	 coprire	 tutti	 i voli	 previsti	 nell’orario.	 Gli	 amministratori	 della	
    compagnia	devono	decidere	quali	voli	 far	partire	e	quali	cancellare.	Progettare	una	
    funzione	select_flights() che,	preso	in	input	l’orario	della	compagnia	ed	il	budget	B,	
    seleziona	quali	voli	far	decollare	in	modo	da	massimizzare	il	numero	complessivo	di	
    posti	 disponibili. Inoltre,	 la	 funzione	 deve	 restituire	 per	 ogni	 areoporto	 a quanti	
    soldi	 devono	 essere	 assegnati	 al	 responsabile	 dello	 scalo	 per	 pagare	 il	 gasolio	
    necessario	per	tutti	i voli	in	partenza	da	a.
"""


def select_flights(flights: List[Flight], budget: int) -> Optional[Tuple[List[Flight], List[Tuple[Airport, int]]]]:
    flights_cost = list()
    num_posti = list()

    # Ordinamento richiede O(nlogn). Reverse richiede O(n) => O(nlogn)
    flights.sort(reverse=True)

    # Inserimento nelle due code O(n)
    for flight in flights:
        num_posti.append(p(flight))
        hours = a(flight) - l(flight)
        flights_cost.append(int(hours.total_seconds() / 60))

    # la funzione max_posti richiede O(n*m)
    list_of_flights = max_posti(flights, flights_cost, num_posti, budget)

    airport_map = {}

    # riempimento lista in O(n)
    for i in list_of_flights:
        dep_airport = i.get_departure_airport()
        elapsed_time = i.get_arrival_time() - i.get_start_time()
        if dep_airport not in airport_map:
            airport_map[dep_airport] = elapsed_time
        else:
            airport_map[dep_airport] += elapsed_time

    return list_of_flights, airport_map


# L'ultiimo elemento è stato preso nella sol ottima dove considero tutti gli elementi e lo zaino di capacità B: se si l'ultimo elemento l'ho inserito
def find_sol(flights, flights_cost, budget, matrix_C):
    n = len(flights)
    sol = list()
    while n - 1 >= 0:
        if matrix_C[n - 1][budget] == True:
            sol.append(flights[n - 1])
            budget = budget - flights_cost[n - 1]
        n -= 1
    return sol


def max_posti(flights, flights_cost, num_posti, budget):
    n = len(flights)
    M = [[0 for k in range(budget + 1)] for i in range(n)]
    C = [[False for k in range(budget + 1)] for i in range(n)]

    for k in range(budget + 1):
        if k > 0 and flights_cost[0] <= k:
            M[0][k] = num_posti[0]
            C[0][k] = True

    for i in range(1, n):
        for k in range(1, budget + 1):
            if flights_cost[i] <= k and (
                    M[i - 1][k - flights_cost[i]] + num_posti[i] >= M[i - 1][k]):  # and c[i] + C[i-1][k-c[i]]<P):
                M[i][k] = M[i - 1][k - flights_cost[i]] + num_posti[i]
                C[i][k] = True
            else:
                M[i][k] = M[i - 1][k]
    return find_sol(flights, flights_cost, budget, C)


def print_select_flight(list, map, budget):
    totale = 0
    tot_seats = 0
    print("Con un budget di {} €  è possibile massimizzare i ricavi con i seguenti voli:".format(budget))
    for i in list:
        dep = i.get_departure_airport().get_name()
        dest = i.get_destination_airport().get_name()
        elapsed_time = i.get_arrival_time() - i.get_start_time()
        seats = i.get_seats()
        tot_seats += seats
        print("- volo da {} a {} di durata {} minuti che trasporta {} passeggeri".format(dep, dest, int(
            elapsed_time.total_seconds() / 60), seats))

    print("\nIl budget deve essere così suddiviso:")
    for i in map:
        costo = int(map.get(i).total_seconds() / 60)
        totale += costo
        print("- aeroporto {}: {} €".format(i.get_name(), costo))

    print("\nPosti totali: {}".format(tot_seats))
    print("Costo totale: {} €".format(totale))
