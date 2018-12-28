from typing import Optional, Dict
from airports_time_schedule.ATS import *


def select_flights(flights: List[Flight], budget: int) -> Optional[Tuple[List[Flight], Dict]]:
    flights_cost = list()
    num_posti = list()

    # Ordinamento richiede O(nlogn)
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
        if matrix_C[n - 1][budget]:
            sol.append(flights[n - 1])
            budget = budget - flights_cost[n - 1]
        n -= 1
    return sol

# I caso inserisco elemento nella soluzione: il costo della soluzione ottima è il costo dell'ultimo elemento più il costo ottimo del sottoproblema dove considero tutti gli altri tranne l'ultimo e la soluzione in cui devo togliere il budget di n
# Sia v vettore dei volumi ,c vettore dei costi
# Devo decidere se mettere o no l'ultimo elemento
# M[n][B] = c_n + M[n-1][n-v_n] (se v_n <= B)
# Se l'ultimo elemento non glielo inserisco: ho n-1 oggetti e il budget è B , in questo caso il costo della soluzione ottima è questo:
# M[n][B] = M[n-1][B]
# Dato che voglio massimizzare il costo scelgo il max tra le due
# v_n capacità dell'ultimo elemento
# M[n][B] = M[n-1][B] if v_n > B
# M[n][B] = max(M[n-1][B],c_n +M[n-1][B-v_n])#Dobbiamo andare a guardare la riga precedente nella matrice (B- v_n)
# Ogni volta abbiamo bisogno anche di M[1][B-v_n], ma v_n non sappiamo quanto vale
# soluzioni al contorno:
# per k = 0,...,B
# M[1][k] = 0 se v_1 > k
# M[1][k] = c_1 otherwise
# Mi calcolo M[1][k] perché ho bisogno per tutta la riga perché non so quanto vale v_n


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


def print_select_flight(flights, airports, budget):
    totale = 0
    tot_seats = 0
    print("With a budget of {} €, you can maximize revenue with the following flights:".format(budget))
    for flight in flights:
        dep = flight.get_departure_airport().get_name()
        dest = flight.get_destination_airport().get_name()
        elapsed_time = flight.get_arrival_time() - flight.get_start_time()
        seats = flight.get_seats()
        tot_seats += seats
        print("- flight from {} to {} - flight duration {} min - passenger {}".format(dep, dest, int(
            elapsed_time.total_seconds() / 60), seats))

    print("\nBudget must be divided as follows:")
    for airport in airports:
        costo = int(airports.get(airport).total_seconds() / 60)
        totale += costo
        print("- airport {}: {} €".format(airport.get_name(), costo))

    print("\nTotal: {} €".format(totale))
    print("Total Seats: {}".format(tot_seats))
