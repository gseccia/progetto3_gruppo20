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


def select_flights(A: List, F: List, B: int) -> Optional[Tuple[List[Flight], List[Tuple[Airport, int]]]]:
    pass
