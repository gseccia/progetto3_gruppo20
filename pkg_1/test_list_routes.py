from pkg_1.list_routes import list_routes
from airports_time_schedule.ATS import *

airports, flights = read_time_schedule_from_files("../airports_time_schedule/airports.csv",
                                                  "../airports_time_schedule/flights.csv")

print("---------------------------------------- TEST_LIST_ROUTES ----------------------------------------")

print("\n---------- Airports ----------")
for airport in airports:
    print_airport(airport)

print("\n---------- Flights ----------")
for flight in flights:
    print_flight(flight)

print("\nDeparture Airport:")
dep_air = airports[0]
print_airport(dep_air)

print("\nDestination Airport:")
dest_air = airports[5]
print_airport(dest_air)

print("\n---------- Possible Routes ----------")
r = list_routes(flights, dep_air, dest_air, datetime.strptime("07:00", "%H:%M"), timedelta(hours=17, minutes=0))
count = 0
if r is not None:
    for path in r:
        print("Route {}".format(count + 1))
        for flight in path:
            print_flight(flight)
        print("\n")
else:
    print("No Path from {} to {}".format(dep_air.get_name(), dest_air.get_name()))
