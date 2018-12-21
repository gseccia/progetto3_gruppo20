import random
from datetime import datetime

from airports_time_schedule.ATS import Airport, Flight


def get_random_pair_airports():
    airports = ["BER", "TXL", "SXF", "BER", "BUH", "OTP", "BBU", "BUE", "EZE", "AEP", "CHI", "ORD", "MDW", "JKT", "CGK",
                "LON", "LHR", "LGW", "LCY", "STN", "LTN", "SEN", "MIL", "MXP", "MIA", "MIA", "MOW", "NYC", "JFK", "CDG",
                "FCO", "CIA", "SAO", "STO", "TYO", "WAS"]
    tmp = random.sample(range(len(airports) - 1), 2)
    list = []
    list.append(Airport(airports[tmp[0]], random.randint(0, 100)))
    list.append(Airport(airports[tmp[1]], random.randint(0, 100)))
    return list


def get_random_flight():
    dep = get_random_pair_airports()[0]
    dest = get_random_pair_airports()[1]
    d = datetime.today()
    d = d.replace(hour=0, minute=0)
    dep_time = get_random_hour(d)
    arr_time = get_random_hour(dep_time)
    seats = random.randint(50, 500)
    flight = Flight(dep, dest, dep_time, arr_time, seats)
    print("Volo {} -> {} - Partenza: {} - Arrivo: {} - Posti {} ".format(
        flight.get_departure_airport().get_name(),
        flight.get_destination_airport().get_name(),
        flight.get_start_time().time().strftime('%H:%M'),
        flight.get_arrival_time().time().strftime('%H:%M'),
        flight.get_seats()))
    return flight


def get_random_hour(start):
    hours = start.hour + random.randint(6, 11)
    minutes = start.minute + random.randint(0, 25)
    start = start.replace(hour=hours, minute=minutes)
    return start


def print_flight(flight):
    print("- Volo da {} a {} con partenza {} e arrivo {} di durata {} minuti che trasporta {} passeggeri".format(
        flight.get_departure_airport().get_name(), flight.get_destination_airport(),
        flight.get_start_time().strftime("%H:%M"),
        flight.get_arrival_time().strftime("%H:%M"), flight.get_elapsed_time(), flight.get_seats()))
