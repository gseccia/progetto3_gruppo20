from pkg_2.find_route import find_route
from airports_time_schedule.ATS import *

airports, flights = read_time_schedule_from_files("../airports_time_schedule/airports.csv",
                                                  "../airports_time_schedule/flights.csv")

print("\n---------- Airports ----------")
for airport in airports:
    print_airport(airport)

print("\n---------- Flights ----------")
for flight in flights:
    print_flight(flight)

print("\nLunghezza lista aeroporti {} - lunghezza lista voli {}".format(len(airports), len(flights)))

print("\nDeparture Airport:")
dep_air = airports[0]
print_airport(dep_air)

print("\nDestination Airport:")
dest_air = airports[5]
print_airport(dest_air)
print("\n")

tmp = find_route(flights, dep_air, dest_air, datetime.strptime("09:00", "%H:%M"))
if tmp is not None:
    print("distance {0}".format(tmp[0]))
    for elem in tmp[1]:
        print(elem)
else:
    print("FUCK OFF")

