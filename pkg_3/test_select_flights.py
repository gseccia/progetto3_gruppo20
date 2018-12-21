import random

from pkg_3.random_test import get_random_flight
from airports_time_schedule.ATS import *
from pkg_3.select_flights import select_flights, print_select_flight

# airports, flights = read_time_schedule_from_files("../airports_time_schedule/airports.csv",
#                                                   "../airports_time_schedule/flights.csv")
# for airport in airports:
#     print(airport)
#     print(c(airport))
# for flight in flights:
#     print(flight)
#     print(p(flight))
#     print(a(flight))
#     print(l(flight))
#     print(d(flight))
#     print(s(flight))

print("---------------------------------------- TEST_SELECT_FLIGHTS ----------------------------------------")
flights = list()
budget = random.randint(500, 3000)
for i in range(10):
    flight = get_random_flight()
    elapsed_time = (flight.get_arrival_time() - flight.get_start_time()) / 60
    flights.append(flight)
print("\n--->")

fly = select_flights(flights, budget)[0]
airport = select_flights(flights, budget)[1]
print_select_flight(fly, airport, budget)