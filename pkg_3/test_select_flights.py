from airports_time_schedule.ATS import *
from pkg_3.select_flights import select_flights


def print_select_flight(flights, airports, budget):
    """
    Metodo di stampa dei voli selezionati
    :param flights: vettore dei voli
    :param airports: vettore degli aereoporti
    :param budget: budget massimo
    :return:
    """
    totale = 0
    tot_seats = 0
    print("With a budget of {} €, you can maximize revenue with the following flights:".format(budget))
    for flight in flights:
        dep = flight.get_departure_airport().get_name()
        dest = flight.get_destination_airport().get_name()
        elapsed_time = flight.get_arrival_time() - flight.get_start_time()
        seats = flight.get_seats()
        tot_seats += seats
        print("- flight from {} to {} - flight duration {} min - passenger {}".format(dep, dest, int(
            elapsed_time.total_seconds() / 60), seats))

    print("\nBudget must be divided as follows:")
    for airport in airports:
        costo = int(airports.get(airport).total_seconds() / 60)
        totale += costo
        print("- airport {}: {} €".format(airport.get_name(), costo))

    print("\nTotal: {} €".format(totale))
    print("Total Seats: {}".format(tot_seats))


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

budget = 400
list_flights = select_flights(flights, budget)[0]
airport = select_flights(flights, budget)[1]
print_select_flight(list_flights, airport, budget)