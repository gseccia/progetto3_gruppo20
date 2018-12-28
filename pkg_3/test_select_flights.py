from airports_time_schedule.ATS import *
from pkg_3.select_flights import select_flights, print_select_flight

print("---------------------------------------- TEST_SELECT_FLIGHTS ----------------------------------------")

airports, flights = read_time_schedule_from_files("../airports_time_schedule/airports.csv",
                                                  "../airports_time_schedule/flights.csv")

print("\n---------- Airports ----------")
for airport in airports:
    print_airport(airport)

print("\n---------- Flights ----------")
for flight in flights:
    print_flight(flight)

print("\n---->")

budget = 400;
list_flights = select_flights(flights, budget)[0]
airport = select_flights(flights, budget)[1]
print_select_flight(list_flights, airport, budget)