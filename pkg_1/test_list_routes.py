from pkg_1.list_routes import list_routes
from airports_time_schedule.ATS import *

airports,flights = read_time_schedule_from_files("../airports_time_schedule/airports.csv", "../airports_time_schedule/flights.csv")
#for airport in airports:
#    print(airport)
#    print(c(airport))
#for flight in flights:
#    print(flight)
#    print(p(flight))
#    print(a(flight))
#    print(l(flight))
#    print(d(flight))
#    print(s(flight))
#print(str(len(airports))+"  "+str(len(flights)))

start=airports[0]
end=airports[5]
print("start ",start)
print("end ",end)
r = list_routes(airports,flights,start,end,datetime.strptime("09:00","%H:%M"), timedelta(hours=17,minutes=0))
for elem in r:
    print(elem)
