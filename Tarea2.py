'''
Created on 10 oct. 2018

@author: fadasgo (Fabio Suarez) y Rosana Garcia
'''
# Carnets 12-10578 y 11-10365

import datetime
from datetime import date

minEdadPensionMujer = 55 # Edad minima para una mujer optar por una pension (sin contar la reduccion de anios por trabajar en medios insalubres)
minEdadPensionHombre = 60 # Edad minima para un hombre optar por una pension (sin contar la reduccion de anios por trabajar en medios insalubres)
minSemanasCotizacionesPension = 750 # numero de semanas minimas cotizadas para optar por una pension

def calcular_edad(fechaNacimiento1):
    hoy = date.today() # hoy equivalente a today
    return hoy.year - fechaNacimiento1.year - ((hoy.month, hoy.day) < (fechaNacimiento1.month, fechaNacimiento1.day))

# verificarFecha chequea si la fecha de nacimiento introducida es correcta o no
def verificarFecha(diaNacimiento,mesNacimiento,anioNacimiento):
    try:
        isinstance(diaNacimiento, int)
        isinstance(mesNacimiento, int)
        isinstance(anioNacimiento, int)
        datetime.datetime(int(anioNacimiento),int(mesNacimiento),int(diaNacimiento))
        return True
            
    except ValueError:
        isValidDate = False
        if(isValidDate) :
            print ("La fecha de nacimiento ingresada es válida")
        else :
            print ("la fecha de nacimiento ingresada no es válida. \n Cada dato debe ser del tipo entero positivo \n")
        return False

# Esta funcion verifica que las semanas cortizadas sean validas 
def verificacionSemCotizadas(semanasCotizadas):
    try:
        isinstance(semanasCotizadas, int)
        if(semanasCotizadas < 0):
            print("El número de semanas cotizadas  no puede ser un entero negativo \n")
            return False
        else:
            return True
    except:
        print("El número de semanas cotizadas es un entero no negativo")
        return False
#print("La edad es: " + str(calcular_edad(datetime.datetime(1995,11,2)))+"años")
#x = verificarFecha(18,12,1988)
#print("La fecha cumple el formato? :" + str(x))
verificacionSemCotizadas(-4)