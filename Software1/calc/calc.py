'''
Tarea 2 Ingeniera de Software I (Version de Entrega)
Created on 10 oct. 2018

@author: fadasgo (Fabio Suarez) y Rosana Garcia
                  Carnets 12-10578 y 11-10365
'''
# Carnets 12-10578 y 11-10365

import datetime
import sys
from datetime import date

minEdadPensionMujer = 55 # Edad minima para una mujer optar por una pension (sin contar la reduccion de anios por trabajar en medios insalubres)
minEdadPensionHombre = 60 # Edad minima para un hombre optar por una pension (sin contar la reduccion de anios por trabajar en medios insalubres)
minSemanasCotizacionesPension = 750 # numero de semanas minimas cotizadas para optar por una pension

def calcular_edad(fechaNacimiento1):
    today = date.today()

    return today.year - fechaNacimiento1.year - ((today.month, today.day) < (fechaNacimiento1.month, fechaNacimiento1.day))

# verificarFecha chequea si la fecha de nacimiento introducida es correcta o no
def verificarFecha(diaNacimiento,mesNacimiento,anioNacimiento):
    try:
        isinstance(diaNacimiento, int)
        isinstance(mesNacimiento, int)
        isinstance(anioNacimiento, int)
        today = date.today()
        if( (anioNacimiento<=today.year) and (mesNacimiento<=12) and (diaNacimiento<=31) ):
            datetime.datetime(int(anioNacimiento),int(mesNacimiento),int(diaNacimiento))
            return True
        else:
            print ("la fecha de nacimiento ingresada no es válida. \n Cada dato debe ser del tipo entero positivo \n")
            return False            
    except ValueError:
        isValidDate = False
        if(isValidDate) :
            print ("La fecha de nacimiento ingresada es válida")
        else :
            print ("la fecha de nacimiento ingresada no es válida. \n Cada dato debe ser del tipo entero positivo \n")
        return False
    
# Esta funcion verifica que las semanas corizadas y años de insalubridad sean validos
def verificacionSemCotizadas(semanasCotizadas):
    try:
        isinstance(semanasCotizadas, int)
        if(semanasCotizadas < 0):
            print("El número de semanas cotizadas  no puede ser un entero negativo \n")
            return False
        else:
            return True
    except:
        print("El número de semanas cotizadas no es suficiente \n")
        return False
        
def verificacionAniosInsalubres(aniosInsalubres):
    try:
        isinstance(aniosInsalubres, int)
        if(aniosInsalubres < 0):
            print("El número de años insalubres laborados por el trabajador no puede ser un entero negativo. \n")
            return False
        else:
            if (aniosInsalubres < 60):
                return True
            else:
                print("El número ingresado excede el numero de años de servicio laboralestablecido por la ley. \n")
                return False
    except:
        return False
        
# Devuelve la cantidad de años de rebaja a la edad minima, si la persona ha trabajado en algun area insalubre
def rebajaPorAniosInsalubres(aniosInsalubres):
    rebaja = 0 # por defecto la cantidad de años es cero si la persona no ha trabajado en un area insalubre
    if(aniosInsalubres <= 20):
        rebaja = aniosInsalubres // 4
        return rebaja
    elif(aniosInsalubres > 20):
        rebaja = 5
        return rebaja
        
# 
'''
verificaSexo:verifica si la persona es hombre o mujer
    Se comprueba si el parámetro es del tipo string, de no ser así se lanza un mensaje de error 
y se cierra el sistema. Retorna True si el sexo es válido y false en caso contrario.
'''
def verificarSexo(string):
    try: 
        isinstance(string, str)
        if(string.lower() == "hombre" or string.lower() == "mujer"):
            return True 
        else:
            print("El sexo debe ser un string. 'hombre' para masculino y ´mujer´ para femenino \n")
            return False

    except:
        print("El sexo debe ser un string. 'hombre' para masculino y ´mujer´ para femenino \n")
        return False
    
def calificaParaLaPension(sexo,diaNacimiento,mesNacimiento,anioNacimiento,semanasCotizadas,aniosInsalubres):
    try:
        x = verificarFecha(diaNacimiento,mesNacimiento,anioNacimiento)
        y = verificacionAniosInsalubres(aniosInsalubres)
        s = verificarSexo(sexo)
        r = verificacionSemCotizadas(semanasCotizadas)
        if((x and y and s and r) == True):
            #print("TODO EXCELENTE")
            fechaNacimiento = datetime.datetime(int(anioNacimiento),int(mesNacimiento),int(diaNacimiento))
            if(minSemanasCotizacionesPension <= semanasCotizadas):
                if(sexo.lower() == "hombre"):
                    if(minEdadPensionHombre <= calcular_edad(fechaNacimiento) + rebajaPorAniosInsalubres(aniosInsalubres)):
                        print("La persona califica para obtener la pensión")
                        return True
                    else:
                        print("La persona no califica para obtener la pensión")
                        return False
                elif(sexo.lower()=="mujer"):
                    if(minEdadPensionMujer <= calcular_edad(fechaNacimiento) + rebajaPorAniosInsalubres(aniosInsalubres)):
                        print("La persona califica para obtener la pensión")
                        return True
                    else:
                        print("La persona no califica para obtener la pensión")
                        return False
            else:
                print("La persona no califica para obtener la pensión")
                return False # la persona no satisface las 750 semanas de cotizacion
        else:
            #print("TODO MAL")
            print("Las condiciones de los datos de entrada no satisfacen la precondicion")
            return False
    
    except ValueError:
        print("Todos los parámetros de la función deben ser enteros mayores o iguales que cero \n")
        return False
#script de prueba
#print("FIN")
#print(calcular_edad(datetime.datetime(1995,11,2)))
#booleano = calificaParaLaPension("MUJER",11, 10, 1964, 750, 20)
#print(booleano)
#x = datetime.datetime(1995,11,2)
#print(x.strftime("%B")) 


#PRUEBAS SOBRE verificarSexo

#1: MUJER
# Valor esperado: True
#print(verificarSexo("MUJER"))
#2: HOMBRE
# Valor esperado: True
#print(verificarSexo("HOMBRE"))
#3:VARIABLE TIPO STRING DISTINTO DE MUJER Y HOMBRE
# Valor esperado: False
#print(verificarSexo("Carapa"))
#4:NUMERO
# Valor esperado: mensaje de error y cierre de sesion
#print(verificarSexo(22))

#PRUEBAS SOBRE LOS AÑOS DE INSALUBRIDAD

#1: Numero positivo
# Valor esperado: True
#print(verificacionAniosInsalubres(20))

#2: Numero negativo
# Valor esperado: False
#print(verificacionAniosInsalubres(-140))

#3: Numero positivo Mayor de 100
# Valor esperado: Mensaje de Confirmación
#print(verificacionAniosInsalubres(140))

#4: valor de tipo String
# Valor esperado: True
#print(verificacionAniosInsalubres("cortaza"))

#5: Valor de tipo booleano
# Valor esperado: True
#print(verificacionAniosInsalubres(True))
