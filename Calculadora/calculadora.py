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

def ejecutar_calculadora():
    print("⋆⭒˚.⋆ Calculadora ⋆⭒˚.⋆")
    
    try:
        # Solicitamos los números al usuario y los convertimos a float
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        print("\n¿Qué querés calcular hoy?")
        print("------------")
        print("|1. Sumar\n|2. Restar\n|3. Multiplicar\n|4. Dividir")
        print("------------")
        opcion = input("Seleccioná (1/2/3/4): ")

        # Lógica de decisión según la opción elegida
        if opcion == '1':
            resultado = sumar(num1, num2)
            simbolo = "+"
        elif opcion == '2':
            resultado = restar(num1, num2)
            simbolo = "-"
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
            simbolo = "*"
        elif opcion == '4':
            resultado = dividir(num1, num2)
            simbolo = "/"
        else:
            print("Opción no válida.")
            return

        # Mostramos el resultado final
        print(f"\nEl resultado de {num1} {simbolo} {num2} es: {resultado} ⋆˚✰ ݁˖⭑")

    except ValueError:
        # Se ejecuta si el usuario ingresa texto en lugar de números
        print("Error: Entrada inválida. Por favor, ingresa solo números.")
    
    except ZeroDivisionError as e:
        # Se ejecuta si el segundo número es cero en una división
        print(f"Error: {e}")
    
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Ocurrió un error inesperado: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_calculadora()