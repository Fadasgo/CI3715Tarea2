''' Casos de prueba (Version de Entrega)
Created on 10 oct. 2018

@author: fadasgo (Fabio Suarez) y Rosana Garcia
'''
# Carnets 12-10578 y 11-10365

import unittest
import calc.calc


class TestCalc(unittest.TestCase):

    def test_calificaParaLaPension(self):

        # Casos True
        # Pruebas de los descuentos de anios por laborar en trabajos insalubres
        print("\n Casos True \n")
        self.assertTrue(calc.calc.calificaParaLaPension("MUJER",9, 10, 1963, 750, 0))
        self.assertTrue(calc.calc.calificaParaLaPension("MUJER",9, 10, 1964, 750, 4))
        self.assertTrue(calc.calc.calificaParaLaPension("MUJER",9, 10, 1965, 750, 8))
        self.assertTrue(calc.calc.calificaParaLaPension("MUJER",9, 10, 1966, 750, 12))
        self.assertTrue(calc.calc.calificaParaLaPension("MuJeR",9, 10, 1967, 750, 16))
        self.assertTrue(calc.calc.calificaParaLaPension("mUjEr",9, 10, 1968, 750, 20))
        self.assertTrue(calc.calc.calificaParaLaPension("hombre",9, 10, 1958, 750, 0)) # caso borde para hombre
        self.assertTrue(calc.calc.calificaParaLaPension("mujer",9, 10, 1968, 750, 20))
        self.assertTrue(calc.calc.calificaParaLaPension("Mujer",11, 10, 1968, 750, 20)) # caso borde el dia de consulta es el mismo dia del cumpleaños
        
        #Casos que retornan False
        print("\n Casos False \n")
        self.assertFalse(calc.calc.calificaParaLaPension("hombre",9, 10, 1958, 0, 0)) # caso borde para hombre, devuelve falso por no cumplir con las semanas de cotizacion
        self.assertFalse(calc.calc.calificaParaLaPension("hombre",9, 10, 1958, 749,20)) # caso borde para hombre, devuelve falso por no cumplir con las semanas de cotizacion
        self.assertFalse(calc.calc.calificaParaLaPension("HOMBRE",12, 10, 1958, 750, 0)) # caso borde el dia de consulta es el dia anterior del cumpleaños
        self.assertFalse(calc.calc.calificaParaLaPension("HOMBRE",15, 10, 1963, 750, 20)) # caso borde el dia de consulta es unos dias antes del cumpleaños, posee la reduccion de los 5 anios
        self.assertFalse(calc.calc.calificaParaLaPension("Mujer",12, 10, 1968, 0, 0)) # caso borde el dia de consulta es el dia anterior del cumpleaños
        self.assertFalse(calc.calc.calificaParaLaPension("HOMBRE",15, 10, 1963, 750, 20)) # caso borde el dia de consulta es unos dias antes del cumpleaños, posee la reduccion de los 5 anios
        self.assertFalse(calc.calc.calificaParaLaPension("mujer",9, 10, 1963, 749,20)) # caso borde para mujer, devuelve falso por no cumplir con las semanas de cotizacion
        self.assertFalse(calc.calc.calificaParaLaPension("HOMBRE",11, 10, 2018, 750, 20)) # Falso ya que nace el mismo día de la consulta
        self.assertFalse(calc.calc.calificaParaLaPension("mujer",11, 10, 2018, 749,20)) # Falso ya que nace el mismo día de la consulta

if __name__ == '__main__':
    unittest.main()