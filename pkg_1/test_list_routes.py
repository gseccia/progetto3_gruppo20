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

print("\n******* CASO 1 *******")
print("Aeroporti selezionati appartenenti alla stessa componente connessa")

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
        count += 1
else:
    print("No Path from {} to {}".format(dep_air.get_name(), dest_air.get_name()))

print("\n******* CASO 2 *******")
print("Aeroporti appartenenti alla stessa componente connessa ma aeroporto di destinazione non raggiungibile")

print("\nDeparture Airport:")
dep_air = airports[8]
print_airport(dep_air)

print("\nDestination Airport:")
dest_air = airports[6]
print_airport(dest_air)

print("\n---------- Possible Routes ----------")
r = list_routes(flights, dep_air, dest_air, datetime.strptime("06:00", "%H:%M"), timedelta(hours=17, minutes=0))
count = 0
if r is not None:
    for path in r:
        print("Route {}".format(count + 1))
        for flight in path:
            print_flight(flight)
        print("\n")
        count += 1
else:
    print("No Path from {} to {}".format(dep_air.get_name(), dest_air.get_name()))

print("\n******* CASO 3 *******")
print("Aeroporti appartenenti a diverse componenti connesse")

print("\nDeparture Airport:")
dep_air = airports[3]
print_airport(dep_air)

print("\nDestination Airport:")
dest_air = airports[7]
print_airport(dest_air)

print("\n---------- Possible Routes ----------")
r = list_routes(flights, dep_air, dest_air, datetime.strptime("05:00", "%H:%M"), timedelta(hours=17, minutes=0))
count = 0
if r is not None:
    for path in r:
        if len(path) > 0:
            print("Route {}".format(count + 1))
            for flight in path:
                print_flight(flight)
            print("\n")
            count += 1
        else:
            print("[]")
else:
    print("No Path from {} to {}".format(dep_air.get_name(), dest_air.get_name()))

print("\n******* CASO 4 *******")
print("Aeroporti di partenza e destinazione coincidono")

print("\nDeparture Airport:")
dep_air = airports[7]
print_airport(dep_air)

print("\nDestination Airport:")
dest_air = airports[7]
print_airport(dest_air)

print("\n---------- Possible Routes ----------")
r = list_routes(flights, dep_air, dest_air, datetime.strptime("05:00", "%H:%M"), timedelta(hours=17, minutes=0))
count = 0
if r is not None:
    for path in r:

        print("Route {}".format(count + 1))
        if len(path)==0:
            print("Stay there!")
        for flight in path:
            print_flight(flight)
        print("\n")
        count += 1
else:
    print("No Path from {} to {}".format(dep_air.get_name(), dest_air.get_name()))


