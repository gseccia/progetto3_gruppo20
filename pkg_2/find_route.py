from typing import Optional
from airports_time_schedule.ATS import *


"""
    Progettare	 una	 funzione	find_route() che,	 preso	in	input	l’orario	 della	 compagnia,	
    gli	areoporti	a e	b,	ed	un	orario	di	partenza	t,	trova	la	rotta	che	permette	di	arrivare	
    da	a a	b nel	minor	tempo	possibile, partendo	ad	un	orario	non	precedente a	t.	(Come	
    per	l’esercizio	precedente,	bisogna	tener	conto	del	tempo	minimo	di	coincidenza	di	
    ogni	scalo).	
"""


def find_route(A: list, F: list, a: str, b: str, t: time) -> Optional[List[Flight]]:
    pass