from __future__ import annotations
from datetime import time
import csv
from typing import List, Tuple
from time import strptime

class Airport:
    __slots__ = ["__c", "__name"]

    def __init__(self, name: str, minimum_time_coincidence_in_minutes: int):
        """
            If minutes are too much for a day
            :raise ValueError
        """
        hours, minutes = divmod(minimum_time_coincidence_in_minutes, 60)
        self.__c = time(hours, minutes)
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_minimum_time_coincidence(self) -> time:
        return self.__c

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__name == other.get_name()
        return False

    def __str__(self):
        return "[name: "+self.__name+", time_needed: "+str(self.__c)+"]"

    def __repr__(self):
        return self.__str__()


class Flight:
    __slots__ = ["__departure_airport", "__destination_airport", "__start_time", "__arrival_time", "__seats"]

    def __init__(self, departure: Airport, destination: Airport, start: time, arrival: time, seats: int):
        self.__departure_airport = departure
        self.__destination_airport = destination
        self.__seats = seats
        self.__start_time = start
        self.__arrival_time = arrival
        self.__seats = seats

    def get_departure_airport(self) -> Airport:
        return self.__departure_airport

    def get_destination_airport(self) -> Airport:
        return self.__destination_airport

    def get_seats(self) -> int:
        return self.__seats

    def get_start_time(self) -> time:
        return self.__start_time

    def get_arrival_time(self) -> time:
        return self.__arrival_time

    def __eq__(self, other):
        if self.__departure_airport == other.get_departure_airport() and \
                self.__destination_airport == other.get_destination_airport() and \
                self.__seats == other.get_seats() and \
                self.__start_time == other.get_start_time() and \
                self.__arrival_time == other.get_arrival_time():
            return True
        return False

    def __str__(self):
        tmp = {"departure": self.__departure_airport, "destination": self.__destination_airport,
               "start": self.__start_time.strftime("%H:%M"), "arrive": self.__arrival_time.strftime("%H:%M"),
               "seats": self.__seats}
        return str(tmp)

    def __repr__(self):
        return self.__str__()


def c(a: Airport) -> time:
    """
    :parameter a: airport to check
    :return: minimum time to take the coincidence
    """
    return a.get_minimum_time_coincidence()


def s(f: Flight) -> Airport:
    """
    :param f: flight to check
    :return: departure airport
    """
    return f.get_departure_airport()


def d(f: Flight) -> Airport:
    """
    :param f: flight to check
    :return: destination airport
    """
    return f.get_destination_airport()


def l(f: Flight) -> time:
    """
    :param f: flight to check
    :return: departure time
    """
    return f.get_start_time()


def a(f: Flight) -> time:
    """
    :param f: flight to check
    :return: arrival time
    """
    return f.get_arrival_time()


def p(f: Flight) -> int:
    """
    :param f: flight to check
    :return:  seats
    """
    return f.get_seats()


def read_time_schedule_from_files(path_to_airports: str = None, path_to_flights: str = None) -> Tuple[List[Airport], List[Flight]]:
    airports = []
    if path_to_airports is not None:
        with open(path_to_airports, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                ap = Airport(row[0], int(row[1]))
                if ap in airports:
                    raise ValueError("Airport "+str(ap)+" duplicated in file.")
                airports.append(ap)

    flights = []
    if path_to_flights is not None:
        with open(path_to_flights, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                found_dest = found_dep = False
                departure = Airport(row[0], 0)
                destination = Airport(row[1], 0)
                for ap in airports:
                    if ap == departure:
                        departure = ap
                        found_dep = True
                    if ap == departure:
                        destination = ap
                        found_dest = True
                if not found_dep:
                    raise ValueError("Departure "+departure.get_name()+" Not found in airports")
                if not found_dest:
                    raise ValueError("Destination "+destination.get_name() + " Not found in airports")

                temp_start = strptime(row[2], "%H:%M")
                temp_arrive = strptime(row[3], "%H:%M")
                start_time = time(temp_start.tm_hour, temp_start.tm_min)
                arrive_time = time(temp_arrive.tm_hour, temp_arrive.tm_min)

                flight = Flight(departure, destination, start_time, arrive_time, int(row[4]))
                if flight not in flights:
                    flights.append(flight)
    return airports, flights


airports, flights = read_time_schedule_from_files("./airports.csv", "./flights.csv")
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
