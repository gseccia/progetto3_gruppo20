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


def select_flights(flights: List[Flight], B: int) -> Optional[Tuple[List[Flight], List[Tuple[Airport, int]]]]:
    nposti = p(flights)
    c = list()
    for flight in flights:
        hours = a(flight)-p(flight)
        c.append(hours.hour*60)

    return max_posti(flights,c,nposti,B)






def find_sol(a, c, d, B,C):  # L'ultiimo elemento è stato preso nella sol ottima dove considero tutti gli elementi e lo zaino di capacità B: se si l'ultimo elemento l'ho inserito
    n = len(a)
    sol = list()
    while n - 1 >= 0:
        if C[n - 1][B] == True:
            sol.append(a[n - 1])
            B = B - c[n - 1]
        n -= 1
    return sol


def max_posti(a, c, d, P):
    solution = dict()
    n = len(a)
    M = [[0 for k in range(P + 1)] for i in range(n)]
    C = [[False for k in range(P + 1)] for i in range(n)]
    for k in range(P + 1):
        if k > 0 and c[0] <= k:
            M[0][k] = d[0]
            C[0][k] = True

    for i in range(1, n):
        for k in range(1, P + 1):
            # Nella k-esima colonna (quando cioè P=k) se la difficoltà che ci sarebbe se l'i-esimo
            # elemento non ci fosse sarebbe minore rispetto a se invece l'avessi inserito,
            # cioè minore della difficoltà totale che è uguale alla somma della sua difficoltà e quella
            # che c'era prima di lui quindi nella colonna k-c[i] e nella riga superiore, inseriscilo e metti cioè la seconda difficoltà
            # l'ultimo elemento lo inserisco anche se la somma dei crediti di entrambi non "appara" a P
            if c[i] <= k and (M[i - 1][k - c[i]] + d[i] >= M[i - 1][k]):  # and c[i] + C[i-1][k-c[i]]<P):
                M[i][k] = M[i - 1][k - c[i]] + d[i]
                C[i][k] = True  # Se abbiamo preso l'ultimo elemento
            #               C[i][k] =C[i-1][k-c[i]] + c[i]
            else:
                M[i][k] = M[i - 1][k]
    #               C[i][k] = C[i-1]
    return M[n - 1][P], find_sol(a, c, d, P, C), M, C
