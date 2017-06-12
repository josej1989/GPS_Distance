#Medición de distancia entre dos puntos gps
from math import radians, sin, cos, atan2, sqrt
radio_tierra = 6371000 #En metros
pto1 = input('latitud, longitud Inicial: ')
pto2 = input('latitud, longitud Final: ')
pto1 = pto1.split(',')
pto2 = pto2.split(',')
dlat = radians(float(pto1[0]) - float(pto2[0]))
dlong = radians(float(pto1[1]) - float(pto2[1]))
lat1 = radians(float(pto1[0]))
lat2 = radians(float(pto2[0]))
a = (sin(dlat/2))**2 + ((sin(dlong/2))**2)*cos(lat1)*cos(lat2)
c = 2 * atan2(sqrt(a), sqrt(1-a))
distancia = c * radio_tierra
print(distancia,'metros')