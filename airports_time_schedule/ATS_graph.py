from __future__ import annotations
from TdP_collections.graphs.graph import Graph
from datetime import datetime, timedelta
import csv
from typing import List, Tuple
from time import strptime


class ATS(Graph):
    class Airport(Graph.Vertex):
        def __init__(self, name: str, minimum_time_coincidence_in_minutes: int):
            """
                If minutes are too much for a day
                :raise ValueError
            """
            hours, minutes = divmod(minimum_time_coincidence_in_minutes, 60)
            super().__init__((name, timedelta(hours=hours, minutes=minutes)))

        def get_name(self) -> str:
            return self.element()[0]

        def get_minimum_time_coincidence(self) -> timedelta:
            return self.element()[1]

        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(id(self.get_name()))

        def __eq__(self, other):
            if type(other) == type(self):
                return self.get_name() == other.get_name()
            return False

        def __str__(self):
            return "[name: "+self.get_name()+", time_needed: "+str(self.get_minimum_time_coincidence())+"]"

        def __repr__(self):
            return self.__str__()

    class Flight(Graph.Edge):
        def __init__(self, departure: ATS.Airport, destination: ATS.Airport, start: datetime, arrival: datetime, seats: int):
            super().__init__(departure,destination,(start,arrival,seats))

        def get_departure_airport(self) -> ATS.Airport:
            return self._origin

        def get_destination_airport(self) -> ATS.Airport:
            return self._destination

        def get_seats(self) -> int:
            return self.element()[2]

        def get_start_time(self) -> datetime:
            return self.element()[0]

        def get_arrival_time(self) -> datetime:
            return self.element()[1]

        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(v, ATS.Airport):
                raise TypeError('v must be an Airport')
            if v is self._origin:
                return self._destination
            elif v is self._destination:
                return self._origin
            raise ValueError('v not incident to edge')

        def __hash__(self):
            return hash((self._origin,self._destination,self.element()))

        def __str__(self):
            tmp = {"departure": self.get_departure_airport(), "destination": self.get_destination_airport(),
                   "start": self.get_start_time().strftime("%H:%M"), "arrive": self.get_arrival_time().strftime("%H:%M"),
                   "seats": self.get_seats()}
            return str(tmp)

        def __repr__(self):
            return self.__str__()

    def _validate_vertex(self, v):
        """Verify that v is a Vertex of this graph."""
        if not isinstance(v, self.Airport):
            raise TypeError('Airport expected')
        if v not in self._outgoing:
            raise ValueError('Airport does not belong to this graph.')

    def insert_vertex(self, x=None, c=None):
        """Insert and return a new Vertex with element x."""
        v = self.Airport(x, c)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    def insert_edge(self, u, v, s=None, a=None, c=None):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Flight(u, v, s, a, c)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def read_time_schedule_from_files(self, path_to_airports: str = None, path_to_flights: str = None) -> List[Airport]:
        airports=[]
        if path_to_airports is not None:
            with open(path_to_airports, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    ap = self.Airport(row[0],int(row[1]))
                    if ap in self.vertices():
                        raise ValueError("Airport " + str(ap) + " duplicated in file.")
                    airports.append(self.insert_vertex(row[0], int(row[1])))

        if path_to_flights is not None:
            with open(path_to_flights, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    found_dest = found_dep = False
                    departure = self.Airport(row[0], 0)
                    destination = self.Airport(row[1], 0)
                    for ap in self.vertices():
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

                    self.insert_edge(departure, destination, start_time, arrive_time, int(row[4]))
        return airports

def c(a: ATS.Airport) -> timedelta:
    """
    :parameter a: airport to check
    :return: minimum time to take the coincidence
    """
    return a.element()[1]


def s(f: ATS.Flight) -> ATS.Airport:
    """
    :param f: flight to check
    :return: departure airport
    """
    return f.get_departure_airport()


def d(f: ATS.Flight) -> ATS.Airport:
    """
    :param f: flight to check
    :return: destination airport
    """
    return f.get_destination_airport()


def l(f: ATS.Flight) -> datetime:
    """
    :param f: flight to check
    :return: departure time
    """
    return f.get_start_time()


def a(f: ATS.Flight) -> datetime:
    """
    :param f: flight to check
    :return: arrival time
    """
    return f.get_arrival_time()


def p(f: ATS.Flight) -> int:
    """
    :param f: flight to check
    :return:  seats
    """
    return f.get_seats()


# g = ATS(True)
# g.read_time_schedule_from_files("./airports.csv", "./flights.csv")
# for airport in g.vertices():
#     print(airport)
#     print(c(airport))
# for flight in g.edges():
#     print(flight)
#     print(p(flight))
#     print(a(flight))
#     print(l(flight))
#     print(d(flight))
#     print(s(flight))
# print(str(len(g.vertices()))+"  "+str(len(g.edges())))
