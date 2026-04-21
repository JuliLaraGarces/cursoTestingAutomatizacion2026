def sumar(a, b):
    #Suma el parámetro A y B
    return a + b

def restar(a, b):
    #Resta el parámetro A y B
    return a - b

def multiplicar(a, b):
    #Multiplica el parámetro A y B
    return a * b

def dividir(a, b):
    #Divide el parámetro A y B
    if b == 0:
        #Lanzo una excepción específica para que el bloque try-except la capture
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b