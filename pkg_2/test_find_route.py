from pkg_2.find_route import find_route
from airports_time_schedule.ATS_graph import *

g = ATS(True)
airports = g.read_time_schedule_from_files("../airports_time_schedule/airports.csv", "../airports_time_schedule/flights.csv")
#for airport in g.vertices():
#    print(airport)
#    print(c(airport))
#for flight in g.edges():
#    print(flight)
#    print(p(flight))
#    print(a(flight))
#    print(l(flight))
#    print(d(flight))
#    print(s(flight))
#print(str(len(g.vertices()))+"  "+str(len(g.edges())))

start=airports[0]
end=airports[5]
print("start ",start)
print("end ",end)
print("distance ",find_route(g,start,end,datetime.strptime("09:00","%H:%M")))

