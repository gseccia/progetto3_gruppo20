from typing import Optional, Dict
from airports_time_schedule.ATS import *


def select_flights(flights: List[Flight], budget: int) -> Optional[Tuple[List[Flight], Dict]]:
    """

    :param flights: lista dei voli
    :param budget: massimo budget raggiungibile
    :return: lista dei voli da prendere per rientrare nel budget e massimizzre i posti, quantità di budget da assegnare a ogni aeroporto
    """
    flights_cost = list()
    num_posti = list()

    # Ordinamento richiede O(nlogn)
    # L'ordinamento dei voli rende possibile, oltre a minimizzare il numero dei posti, anche a ridurre il budget totale da spendere
    flights_sorted = sorted(flights, reverse=True, key=lambda flight: (l(flight)-a(flight)))

    # Inserimento nelle due code O(n)
    for flight in flights_sorted:
        num_posti.append(p(flight))
        hours = a(flight) - l(flight)
        flights_cost.append(int(hours.total_seconds() / 60))

    # la funzione max_posti richiede O(n*B) (B=budget)
    list_of_flights = max_posti(flights_sorted, flights_cost, num_posti, budget)

    airport_map = {}

    for i in list_of_flights:
        dep_airport = s(i)
        cost_flight = int((a(i) - l(i)).total_seconds() / 60)
        if dep_airport not in airport_map:
            airport_map[dep_airport] = cost_flight
        else:
            airport_map[dep_airport] += cost_flight

    return list_of_flights, airport_map


# L'ultimo elemento è stato preso nella sol ottima dove considero tutti gli elementi ed è stato raggiunto il budget B:
# si considera sempre l'ultimo elemento e se è stato inserito si ripercorre la matrice per trovare quali altri voli sono stati scelti nella soluzione
def find_sol(flights, flights_cost, budget, matrix_C):
    """

    :param flights: vettore dei voli
    :param flights_cost: vettore dei costi di ogni volo
    :param budget: massimo budget spendibile
    :param matrix_C: matrice della soluzione
    :return: la lista dei voli da prendere per massimizzare il numero dei posti
    """
    n = len(flights)
    sol = list()
    while n - 1 >= 0:
        if matrix_C[n - 1][budget]:
            sol.append(flights[n - 1])
            budget = budget - flights_cost[n - 1]
        n -= 1
    return sol


def max_posti(flights, flights_cost, num_posti, budget):
    """
    :param flights:
    :param flights_cost:
    :param num_posti:
    :param budget:
    :return: il metodo find_sol
    """
    n = len(flights)
    #Per svolgere il problema facciamo uso di una matrice M dove la cella i,j rappresenta il costo totale raggiunto
    #all'elemento i e al budget massimo j
    M = [[0 for k in range(budget + 1)] for i in range(n)]
    #La matrice C sarà una matrice 0/1 la cui cella i,j sarà 1 se l'elemento i è stato preso quanod il budget massimo è j, altrimenti 0
    C = [[False for k in range(budget + 1)] for i in range(n)]
    #Si riempie la prima riga della matrice poiché per ogni riga mi serve la riga precedente per ottenere la soluzione ottima
    for k in range(budget + 1):
        if k > 0 and flights_cost[0] <= k:
            M[0][k] = num_posti[0]
            C[0][k] = True


    for i in range(1, n):
        for k in range(1, budget + 1):

            #Devo decidere se prendere l'i-esimo elemento
            # I caso-> inserisco elemento nella soluzione:
            #La soluzione ottima si ottiene prendendo l'elemento, in quanto se non prendessi l'elemento
            #la soluzione ottenuta sarebbe minore rispetto a quella che si ottiene se invece prendessi l'elemento
            # il costo della soluzione ottima è il costo dell'ultimo elemento più il costo ottimo del sottoproblema dove considero tutti gli altri tranne l'ultimo e la soluzione in cui devo togliere il budget di n
            if flights_cost[i] <= k and (M[i - 1][k - flights_cost[i]] + num_posti[i] >= M[i - 1][k]):

                M[i][k] = M[i - 1][k - flights_cost[i]] + num_posti[i]
                C[i][k] = True
            else:
                M[i][k] = M[i - 1][k] # II caso -> non inserisco elemento nella soluzione:

    #La soluzione ottima è contenuta nella matrice C
    return find_sol(flights, flights_cost, budget, C)


