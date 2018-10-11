'''
Created on 10 oct. 2018

@author: fadasgo (Fabio Suarez) y Rosana Garcia
'''
#Carnets 12-10578 y 11-10365

import datetime
from datetime import date

minEdadPensionMujer = 55 # Edad minima para una mujer optar por una pension (sin contar la reduccion de anios por trabajar en medios insalubres)
minEdadPensionHombre = 60 # Edad minima para un hombre optar por una pension (sin contar la reduccion de anios por trabajar en medios insalubres)
minSemanasCotizacionesPension = 750 # numero de semanas minimas cotizadas para optar por una pension

def calcular_edad(fechaNacimiento1):
    hoy = date.today() # hoy equivalente a today
    return hoy.year - fechaNacimiento1.year - ((hoy.month, hoy.day) < (fechaNacimiento1.month, fechaNacimiento1.day))

print("La edad es: " + str(calcular_edad(datetime.datetime(1995,11,2)))+"años")