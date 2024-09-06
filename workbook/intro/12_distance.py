from math import radians
from cmath import acos, sin, cos

lat1 = radians(float(input("Enter Latitude 1: ")))
lng1 = radians(float(input("Enter Longitude 2: ")))

lat2 = radians(float(input("Enter Latitude 2: ")))
lng2 = radians(float(input("Enter Longitude 2: ")))

distance = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lng1 - lng2))

print(distance)
