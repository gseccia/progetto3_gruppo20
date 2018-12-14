from typing import Optional
from airports_time_schedule.ATS_graph import *

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
def list_routes(ts: ATS, a: str, b: str, t: time, T: int) -> Optional[List[List[ATS.Flight]]]:
    """

    :param ts: Orario della compagnia
    :param a: Identificativo aereoporto di partenza
    :param b: Identificativo aereoporto di arrivo
    :param t: Orario minimo di partenza
    :param T: Tempo massimo richiesto della rotta
    :return: Lista di liste di voli richiesti, oppure None se nessun volo soddisfa le specifiche
    """
    pass

def find_one_root(ts: ATS, a: str, b: str, t: time, T: int) -> Optional[List[ATS.Flight]]:
    pass