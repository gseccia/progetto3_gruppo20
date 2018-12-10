from __future__ import annotations
from datetime import time
from time import strptime
import csv
from TdP_collections.graphs.graph import Graph


class ATS(Graph):
    # ------------------------- nested Vertex class -------------------------
    class Airport(Graph.Vertex):
        """Lightweight vertex structure for a graph."""

        # noinspection PyCompatibility
        def __init__(self, x, ct):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            hours, minutes = divmod(ct, 60)
            tmp = time(hours, minutes)
            super().__init__((x, tmp))

        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return "[name: " + self.element()[0] + ", time_needed: " + str(self.element()[1]) + "]"

        def __repr__(self):
            return self.__str__()

    # ------------------------- nested Edge class -------------------------
    class Flight(Graph.Edge):
        """Lightweight edge structure for a graph."""

        # noinspection PyCompatibility
        def __init__(self, u, v, start, arrival, seats):
            """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
            super().__init__(u, v, (start, arrival, seats))

        # Override
        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(v, ATS.Flight):
                raise TypeError('v must be a Flight')
            if v is self._origin:
                return self._destination
            elif v is self._destination:
                return self._origin
            raise ValueError('Airport not incident to flight')

        def __str__(self):
            tmp = {"departure": self._origin, "destination": self._destination,
                   "start": self._element[0].strftime("%H:%M"), "arrive": self._element[1].strftime("%H:%M"),
                   "seats": self._element[2]}
            return str(tmp)

        def __repr__(self):
            return self.__str__()

    # ------------------------- Graph methods -------------------------
    # noinspection PyCompatibility
    def __init__(self, directed=False,path_to_flights=None):
        """Create an empty graph (undirected, by default).

        Graph is directed if optional paramter is set to True.
        """
        super().__init__(directed)
        if path_to_flights is not None:
            self.read_flights_from_file(path_to_flights)

    # Override
    def _validate_vertex(self, v):
        """Verify that v is a Vertex of this graph."""
        if not isinstance(v, self.Airport):
            raise TypeError('Airport expected')
        if v not in self._outgoing:
            raise ValueError('Airport does not belong to this graph.')

    # Override
    def insert_vertex(self, x=None, time=None):
        """Insert and return a new Vertex with element x."""
        v = self.Airport(x, time)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    # Override
    def insert_edge(self, u, v, start=None, arrive=None, seats=None):
        """Insert and return a new Edge from u to v with auxiliary element x.

    Raise a ValueError if u and v are not vertices of the graph.
    Raise a ValueError if u and v are already adjacent.
    """
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Flight(u, v, start, arrive, seats)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    # added
    def read_flights_from_file(self, path=None):
        if path is not None:
            with open(path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    departure = self.insert_vertex(row[0], int(row[1]))

                    destination = self.insert_vertex(row[2], int(row[3]))

                    temp_start = strptime(row[4], "%H:%M")
                    temp_arrive = strptime(row[5], "%H:%M")
                    start_time = time(temp_start.tm_hour, temp_start.tm_min)
                    arrive_time = time(temp_arrive.tm_hour, temp_arrive.tm_min)
                    self.insert_edge(departure, destination, start_time, arrive_time, int(row[6]))

    # added
    def read_airports_from_file(self, path=None):
        if path is not None:
            with open(path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.insert_vertex(row[0], int(row[1]))


def c(a: ATS.Airport):
    """
    :parameter a: airport to check
    :return: minimum time to take the coincidence
    """
    return a.element()[1]


def s(f: ATS.Flight):
    """
    :param f: flight to check
    :return: departure airport
    """
    return f.endpoints()[0]


def d(f: ATS.Flight):
    """
    :param f: flight to check
    :return: destination airport
    """
    return f.endpoints()[1]


def l(f: ATS.Flight):
    """
    :param f: flight to check
    :return: departure time
    """
    return f.element()[0]


def a(f: ATS.Flight):
    """
    :param f: flight to check
    :return: arrival time
    """
    return f.element()[1]


def p(f: ATS.Flight):
    """
    :param f: flight to check
    :return:  seats
    """
    return f.element()[2]


ats = ATS(True, "./flights.csv")
for vertex in ats.vertices():
    print(vertex)
    print(c(vertex))
for edge in ats.edges():
    print(edge)
    print(p(edge))
    print(a(edge))
    print(l(edge))
    print(d(edge))
    print(s(edge))
