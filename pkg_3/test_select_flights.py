from pkg_3.select_flights import select_flights
from airports_time_schedule.ATS import *

airports,flights = read_time_schedule_from_files("../airports_time_schedule/airports.csv", "../airports_time_schedule/flights.csv")
for airport in airports:
    print(airport)
    print(c(airport))
for flight in flights:
    print(flight)
    print(p(flight))
    print(a(flight))
    print(l(flight))
    print(d(flight))
    print(s(flight))
print(str(len(airports))+"  "+str(len(flights)))

a,b =select_flights(flight,100)
