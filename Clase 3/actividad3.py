#Refactorizar el script de la calculadora lineal en al menos 4 funciones separadas. 
# una por cada tipo de operación. Como ser: Sumar(), Restar(), Multiplicar() y Dividir()
#Añadir manejo de excepciones para entradas inválidas y división por cero.


def Sumar(primero,segundo):
    primerNumeroSumar = float(input(f"Ingrese por favor su primer número a sumar"))
    segundoNumeroSumar = float(input(f"Ingrese por favor su segundo número a sumar"))
    primero = primerNumeroSumar
    segundo = segundoNumeroSumar
    resultado = primerNumeroSumar + segundoNumeroSumar
    print(f"La suma de los números: {primerNumeroSumar} + {segundoNumeroSumar} es igual a: {resultado}")
