from datetime import datetime, timedelta
import csv
from typing import List, Tuple, Dict


class Airport:
    __slots__ = ["__c", "__name"]

    def __init__(self, name: str, minimum_time_coincidence_in_minutes: int):
        """
            If minutes are too much for a day
            :raise ValueError
        """
        hours, minutes = divmod(minimum_time_coincidence_in_minutes, 60)
        self.__c = timedelta(hours=hours, minutes=minutes)
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_minimum_time_coincidence(self) -> timedelta:
        return self.__c

    def __hash__(self):
        return hash(id(self.__name))

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__name == other.get_name()
        return False

    def __str__(self):
        return "Airport {} - Coincidence: {}".format(self.get_name(), self.get_minimum_time_coincidence())

    def __repr__(self):
        return self.__str__()


class Flight:
    __slots__ = ["__departure_airport", "__destination_airport", "__start_time", "__arrival_time", "__seats"]

    def __init__(self, departure: Airport, destination: Airport, start: datetime, arrival: datetime, seats: int):
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

    def get_elapsed_time(self) -> int:
        return int((self.__arrival_time - self.__start_time).total_seconds() / 60)

    def get_start_time(self) -> datetime:
        return self.__start_time

    def get_arrival_time(self) -> datetime:
        return self.__arrival_time

    def __eq__(self, other):
        if not (type(self) is type(other)):
            raise (ValueError("The type must be instances of Flight"))
        if self.__departure_airport == other.get_departure_airport() and \
                self.__destination_airport == other.get_destination_airport() and \
                self.__seats == other.get_seats() and \
                self.__start_time == other.get_start_time() and \
                self.__arrival_time == other.get_arrival_time():
            return True
        return False

    def __str__(self):
        return "Flight {} -> {} - Departure: {} - Arrival: {} - Seats {} ".format(
            self.get_departure_airport().get_name(),
            self.get_destination_airport().get_name(),
            self.get_start_time().time().strftime('%H:%M'),
            self.get_arrival_time().time().strftime('%H:%M'),
            self.get_seats())

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(
            str(self.__departure_airport) + str(self.__destination_airport) + str(self.__seats) + str(self.__start_time) + str(self.__arrival_time))


def c(a: Airport) -> timedelta:
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


def l(f: Flight) -> datetime:
    """
    :param f: flight to check
    :return: departure time
    """
    return f.get_start_time()


def a(f: Flight) -> datetime:
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


def read_time_schedule_from_files(path_to_airports: str = None, path_to_flights: str = None) -> Tuple[
    List[Airport], List[Flight]]:
    airports = []
    if path_to_airports is not None:
        with open(path_to_airports, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                ap = Airport(row[0], int(row[1]))
                if ap in airports:
                    raise ValueError("Airport " + str(ap) + " duplicated in file.")
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
                    if ap == destination:
                        destination = ap
                        found_dest = True
                if not found_dep:
                    raise ValueError("Departure " + departure.get_name() + " Not found in airports")
                if not found_dest:
                    raise ValueError("Destination " + destination.get_name() + " Not found in airports")

                start_time = datetime.strptime(row[2], "%H:%M")
                arrive_time = datetime.strptime(row[3], "%H:%M")

                flights.append(Flight(departure, destination, start_time, arrive_time, int(row[4])))
    return airports, flights
