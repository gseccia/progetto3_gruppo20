from __future__ import annotations
from datetime import time
import csv
from typing import List
from time import strptime
from TdP_collections.graphs import graph
# read a time from string
# temp = strptime(string_time in format HH:MM, "%H:%M")
# time = time(temp.tm_hour, temp.tm_min)


class Airport:
    __slots__ = ["__c", "__name"]

    def __init__(self, name: str, minimum_time_coincidence_in_minutes: int):
        """
            If minutes are too much for a day
            :raise ValueError
        """
        hours, minutes = divmod(minimum_time_coincidence_in_minutes, 60)
        self.__c = time(hours, minutes)

    def get_name(self) -> str:
        return self.__name

    def get_minimum_time_coincidence(self) -> time:
        return self.__c

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__name == other.get_name()
        elif type(other) is str:
            return self.__name == other

    def __str__(self):
        return "[name: "+self.__name+", time_needed: "+str(self.__c)+"]"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def read_airports_from_file(path: str = None) -> List[Airport]:
        airports_list = []
        if path is not None:
            with open(path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    airports_list.append(Airport(row[0], int(row[1])))
        return airports_list


class Flight:
    __slots__ = ["__departure_airport", "__destination_airport", "__start_time", "__arrival_time", "__seats"]

    def __init__(self, departure: str, destination: str, start: time, arrival: time, seats: int):
        self.__departure_airport = departure
        self.__destination_airport = destination
        self.__seats = seats
        self.__start_time = start
        self.__arrival_time = arrival
        self.__seats = seats

    def get_departure_airport(self) -> str:
        return self.__departure_airport

    def get_destination_airport(self) -> str:
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
                self.__arrival_time == other.__arrival_time():
            return True
        return False

    def __str__(self):
        tmp = {"departure": self.__departure_airport, "destination": self.__destination_airport,
               "start": self.__start_time.strftime("%H:%M"), "arrive": self.__arrival_time.strftime("%H:%M"),
               "seats": self.__seats}
        return str(tmp)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def read_flights_from_file( path: str) -> List[Flight]:
        flights_list = []
        if path is not None:
            with open(path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    temp_start = strptime(row[2], "%H:%M")
                    temp_arrive = strptime(row[3], "%H:%M")
                    start_time = time(temp_start.tm_hour, temp_start.tm_min)
                    arrive_time = time(temp_arrive.tm_hour, temp_arrive.tm_min)
                    flights_list.append(Flight(row[0], row[1], start_time, arrive_time, int(row[4])))
        return flights_list


def c(a: Airport) -> time:
    """
    :parameter a: airport to check
    :return: minimum time to take the coincidence
    """
    return a.get_minimum_time_coincidence()


def s(f: Flight) -> str:
    """
    :param f: flight to check
    :return: departure airport
    """
    return f.get_departure_airport()


def d(f: Flight) -> str:
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


list = ATS.read_airports_from_file("./airports.csv")
print(list)
print(list[0] == "AAB")
print(list[0] == list[3])

list = ATS.read_flights_from_file("./flights.csv")
print(list)
