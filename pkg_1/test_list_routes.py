from pkg_1.list_routes import list_routes
from airports_time_schedule.ATS import *
from pkg_3.random_test import *

airports,flights = read_time_schedule_from_files("../airports_time_schedule/airports.csv", "../airports_time_schedule/flights.csv")
"""
start=airports[0]
end=airports[5]
print("start ",start)
print("end ",end)
r = list_routes(flights,start,end,datetime.strptime("09:00","%H:%M"), timedelta(hours=17,minutes=0))
if r is not None:
    for elem in r:
        print(elem)
else:
    print("empty path")
"""

tmp_flight = list()
for i in range(2):
    tmp_flight.append(get_random_flight())

r = list_routes(tmp_flight,s(tmp_flight[0]), d(tmp_flight[0]),datetime.strptime("00:00","%H:%M"), timedelta(hours=24,minutes=0))
if len(r) is not 0:
    for elem in r:
        print(elem)
else:
    print("empty path")
